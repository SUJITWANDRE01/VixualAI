import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display, Markdown
from PIL import Image
from dotenv import load_dotenv
import os
from transformers import BertForQuestionAnswering, BertTokenizer
import torch
import numpy as np
import warnings
from transformers import logging
from flask import Flask, render_template, request, jsonify
import io
import base64

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Some weights of the model checkpoint at")
logging.set_verbosity_error()

# Load the environment variables from the .env file
load_dotenv()

# Access the GEMINI_API_KEY from the .env file
api_key = os.getenv("GEMINI_API_KEY")

# Configure Generative AI with the loaded API key
genai.configure(api_key=api_key)

# Load BERT tokenizer and model for question answering
tokenizer2 = BertTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model2 = BertForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

# Helper function to format text as Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Flask app setup
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model1')
def model1_page():
    return render_template('model1.html')

@app.route('/model2')
def model2_page():
    return render_template('model2.html')

@app.route('/model3')
def model3_page():
    return render_template('model3.html')

@app.route('/generate_description', methods=['POST'])
def generate_description():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    img_file = request.files['image']
    img_bytes = img_file.read()
    img = Image.open(io.BytesIO(img_bytes))

    # Generate content using the Gemini model
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
    )

    prompt = "Describe the image in detail, focusing on the key objects, people, and their actions, colours in simple terms with neat explanation."
    response = model.generate_content([{'mime_type': 'image/jpeg', 'data': base64.b64encode(img_bytes).decode('utf-8')}, prompt])

    description = response.text.strip().replace('\n', ' ')
    return jsonify({'description': description})

@app.route('/get_answer', methods=['POST'])
def get_answer():
    question = request.form['question']
    passage = request.form['passage']
    answer = bert_question_answer(question, passage)
    return jsonify(answer)

def bert_question_answer(question, passage, max_len=500):
    input_ids = tokenizer2.encode(question, passage, max_length=max_len, truncation=True)
    sep_index = input_ids.index(102)
    len_question = sep_index + 1
    len_passage = len(input_ids) - len_question
    segment_ids = [0] * len_question + [1] * len_passage

    start_token_scores = model2(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]))[0]
    end_token_scores = model2(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]))[1]

    start_token_scores = start_token_scores.detach().numpy().flatten()
    end_token_scores = end_token_scores.detach().numpy().flatten()

    answer_start_index = np.argmax(start_token_scores)
    answer_end_index = np.argmax(end_token_scores)

    start_token_score = np.round(start_token_scores[answer_start_index], 2)
    end_token_score = np.round(end_token_scores[answer_end_index], 2)

    tokens = tokenizer2.convert_ids_to_tokens(input_ids)
    answer = tokens[answer_start_index]
    for i in range(answer_start_index + 1, answer_end_index + 1):
        if tokens[i][0:2] == '##':
            answer += tokens[i][2:]
        else:
            answer += ' ' + tokens[i]

    if (start_token_score < 0) or (answer_start_index == 0) or (answer_end_index < answer_start_index) or (answer == '[SEP]'):
        answer = "Sorry!, I was unable to discover an answer in the passage."

    return answer

@app.route('/generate_and_answer', methods=['POST'])
def generate_and_answer():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    img_file = request.files['image']
    img_bytes = img_file.read()
    img = Image.open(io.BytesIO(img_bytes))

    # Generate content using the Gemini model
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
    )

    prompt = "Describe the image in detail, focusing  on the key objects, people, and their actions, colours in simple terms with neat explanation."
    response = model.generate_content([{'mime_type': 'image/jpeg', 'data': base64.b64encode(img_bytes).decode('utf-8')}, prompt])

    description = response.text.strip().replace('\n', ' ')

    question = request.form['question']
    answer = bert_question_answer(question, description)

    return jsonify({'description': description, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)