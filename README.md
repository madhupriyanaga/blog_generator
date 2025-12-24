# Blog Generator with LLaMA 2 and Hugging Face

## Overview
The Blog Generator is an AI-powered application that creates high-quality blog posts based on user-provided topics. It leverages advanced language models from Hugging Face to generate content in various tones and lengths.

## Features
- **Customizable Blog Generation**: Choose the tone and length of your blog.
- **AI-Powered Content**: Uses state-of-the-art language models for text generation.
- **User-Friendly Interface**: Built with Streamlit for an intuitive user experience.

## Prerequisites
- Python 3.8 or higher
- Internet connection (to download models from Hugging Face)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd src/blog_generator
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. Start the backend:
   ```bash
   python backend/app.py
   ```
2. Start the frontend:
   ```bash
   streamlit run frontend/app.py
   ```
3. Open the application in your browser and start generating blogs!

## How It Works
1. **User Input**: Enter a topic, select the tone, and specify the desired blog length.
2. **AI Generation**: The backend uses Hugging Face Transformers to generate the blog content.
3. **Output**: The generated blog is displayed in the frontend.

## Models Used
- Default: GPT-2
- Replaceable with other Hugging Face models (e.g., GPT-Neo, OPT, LLaMA).

## Customization
To use a different model, update the `model` parameter in `backend/app.py`:
```python
generator = pipeline("text-generation", model="your-model-name")
```
