# FastAPI AI Model Backend
This repository contains a FastAPI application that leverages Hugging Face Transformers to provide AI capabilities, including sentiment analysis and text generation. The app is designed to be straightforward, allowing you to interact with various pre-trained models via HTTP requests.

## Features
- **Sentiment Analysis**: Determine the sentiment of input text (positive or negative).
- **Text Generation**: Generate text responses based on questions.

## Technologies Used
- **FastAPI**: A modern, high-performance web framework for building APIs with Python.
- **Hugging Face Transformers**: A library that offers a variety of pre-trained models for Natural Language Processing (NLP).
- **Uvicorn**: An ASGI server for running FastAPI applications.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

### Clone the Repository
Clone the repository: `git clone <repository-url> && cd <repository-directory>`

### Install Dependencies
Install dependencies: `pip install fastapi uvicorn transformers torch`

### Start the Backend
Start the backend: `uvicorn app:app --host 127.0.0.1 --port 8000 --reload`

## Testing the API Endpoints
To check if the API is running, use the following command: `curl -X GET http://127.0.0.1:8000/` 
Expected Response: `{"message": "AI model backend running"}` 

To analyze the sentiment of a given text, use the following command: `curl -X POST http://127.0.0.1:8000/predict/ -H "Content-Type: application/json" -d "{\"text\": \"Your text here\"}"` 
Expected Response: `{"prediction": [ { "label": "POSITIVE", "score": 0.999 } ] }` 

To generate a response to a question, use the following command: `curl -X POST http://127.0.0.1:8000/ask/ -H "Content-Type: application/json" -d "{\"question\": \"Your question here\"}"` 
Expected Response: `{"answer": "Generated response here"}`


## How It All Comes Together
FastAPI serves as the backend framework that handles incoming HTTP requests and routes them to the appropriate functions. Hugging Face Transformers provides pre-trained models that can be utilized for various NLP tasks. In this application, we use models for sentiment analysis and text generation. When a user makes a request to an endpoint, FastAPI receives the request, processes the input, and calls the respective Hugging Face model pipeline to generate a response. The response is then returned to the user in a structured JSON format.

## Conclusion
This FastAPI application demonstrates how to integrate multiple Hugging Face models into a single backend service. You can easily extend it by adding more models or endpoints as needed. Feel free to explore and modify the application to suit your needs!

## Notes
Ensure your Python environment is properly set up before running the application. Depending on the models you use, additional memory and CPU resources may be required, especially for larger models.
