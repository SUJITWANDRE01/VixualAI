# Vixual

This project integrates three different AI models into a Flask web application, allowing users to upload images, generate descriptions, and ask questions based on the generated descriptions. The application uses generative AI for image description generation and BERT for question answering.

## ✨Features
1. **Image Description Generation**:
   - Upload an image to generate a detailed description, including information such as color, products, texture, lighting, scale, movement, emotion, and context.
   
2. **Question Answering**:
   - Upload a passage and a question to get an answer using a pre-trained BERT model for question answering.

3. **Generate & Answer**:
   - Upload an image, generate its description, and ask a question about the generated description. The application will provide an answer based on the description.

## 🛠Requirements

- Python 3.12
- Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## 📦 Dependencies
**Flask**: Web framework for the app.

**transformers**: Hugging Face library for BERT-based models.

**google-generativeai**: For working with Google’s Generative AI model.

**torch**: For deep learning model processing.

**Pillow**: Image processing.

**dotenv**: To load environment variables from .env file.

**IPython**: Displaying markdown in Jupyter Notebooks.

## ⚙️Setup
1. **Create an .env file**:
   - You need to set up a **.env** file to securely store your API keys and other sensitive information.
   - Example .env file:
  
   ```bash
   API_KEY=<YOUR_GOOGLE_API_KEY>
   ```


2. **Run the Application**:

   - Once the dependencies are installed and the .env file is configured, you can start the Flask app with:
   ```bash
   python app.py
   ```

## 📌Notes
  - Make sure the .env file contains the correct API keys, especially for Google’s Gemini AI API.
  - The models used for generating descriptions and answering questions require substantial resources. If running on a local machine, consider using a GPU for improved          performance.
   - You can modify the model parameters or error handling based on your specific needs.
   - The app uses Flask to handle routes, and you’ll need to have a basic understanding of web development to customize it further.
   - The app’s front-end pages (HTML templates) are located in the templates/ folder.

## 🚀 Generate Your Gemini API Key : 
   - To begin using the Google Gemini API and integrate it with this application, you'll need to generate an API key. Follow the link below to create your API key:
       ```bash
        https://ai.google.dev/gemini-api/docs?gad_source=1&gclid=CjwKCAiApY-7BhBjEiwAQMrrEVoS1V8KDO-PuP0DSGelIc_jx85Z3114kP5WF0M7DCD4PxaC48YEehoCt1EQAvD_BwE
       ```
