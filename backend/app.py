import os
import random
from transformers import pipeline, set_seed

# Initialize the text generation pipeline
def initialize_generator():
    """
    Initialize the text generation pipeline using Hugging Face Transformers.
    Returns:
        generator: A text generation pipeline object.
    """
    try:
        generator = pipeline("text-generation", model="gpt2")  # Replace "gpt2" with your desired model
        set_seed(42)  # Set a seed for reproducibility
        return generator
    except Exception as e:
        raise RuntimeError(f"Error initializing the text generation pipeline: {e}")

# Generate a blog based on the given topic
def generate_blog(topic, blog_length=200, tone="Professional"):
    """
    Generate a blog based on the given topic, length, and tone.

    Args:
        topic (str): The topic for the blog.
        blog_length (int): The desired length of the blog in words.
        tone (str): The tone of the blog (e.g., Professional, Casual, etc.).

    Returns:
        str: The generated blog content.
    """
    generator = initialize_generator()

    # Define a prompt based on the topic and tone
    prompt = f"Write a {tone.lower()} blog about '{topic}'.

    try:
        # Generate text using the pipeline
        output = generator(prompt, max_length=blog_length, num_return_sequences=1)
        blog_content = output[0]["generated_text"]
        return blog_content
    except Exception as e:
        return f"Error generating blog: {e}"
