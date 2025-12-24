# Blog Generator

## Overview
The Blog Generator is a Streamlit-based web application that leverages the LLaMA 2 model to generate high-quality blog posts. Users can input a topic, customize the tone and length of the blog, and generate content instantly.

## Features
- **Customizable Blog Generation**: Adjust the tone (e.g., Professional, Casual, Informative, Persuasive) and length (100-500 words).
- **Interactive User Interface**: Built with Streamlit for a seamless user experience.
- **AI-Powered Content Creation**: Utilizes LLaMA 2 for generating high-quality, contextually relevant blog content.

## How It Works
1. **Input**: Enter a blog topic in the text input field.
2. **Customize**: Select the desired tone and adjust the blog length using the sidebar settings.
3. **Generate**: Click the "Generate Blog" button to create a blog post.
4. **Output**: View the generated blog post in the main content area.

## Prerequisites
- Python 3.8 or higher
- Streamlit

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd blog_generator
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. Ensure the backend script `app.py` is located in the `backend` folder.
2. Start the Streamlit app:
   ```bash
   streamlit run frontend/app.py
   ```
3. Open the app in your browser at `http://localhost:8501`.

## Notes
- The backend script `app.py` in the `backend` folder must include a `generate_blog(topic)` function that returns the generated blog content.
- Customize the app's appearance using the provided CSS in `frontend/app.py`.

## License
This project is licensed under the MIT License.
