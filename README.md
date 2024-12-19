# Flask AI Model Integration

This project integrates three different AI models into a Flask web application, allowing users to upload images, generate descriptions, and ask questions based on the generated descriptions. The application uses generative AI for image description generation and BERT for question answering.

## Features
1. **Image Description Generation**:
   - Upload an image to generate a detailed description, including information such as color, products, texture, lighting, scale, movement, emotion, and context.
   
2. **Question Answering**:
   - Upload a passage and a question to get an answer using a pre-trained BERT model for question answering.

3. **Generate & Answer**:
   - Upload an image, generate its description, and ask a question about the generated description. The application will provide an answer based on the description.

## Requirements

- Python 3.12
- Install dependencies using `pip`:

```bash
pip install -r requirements.txt

## Dependencies
Flask: Web framework for the app
transformers: Hugging Face library for BERT-based models
google-generativeai: For working with Google’s Generative AI model
torch: For deep learning model processing
Pillow: Image processing
dotenv: To load environment variables from .env file
IPython: Displaying markdown in Jupyter Notebooks
