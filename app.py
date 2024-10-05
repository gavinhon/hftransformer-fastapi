from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load pre-trained sentiment analysis, extractive Q&A, and generative models
nlp_sentiment = pipeline('sentiment-analysis')
nlp_chatgpt = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')  # Using GPT-Neo 2.7B for generative responses

# Define request body models
class TextInput(BaseModel):
    text: str

class QuestionOnlyInput(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"message": "AI model backend running"}

@app.post("/predict/")
def predict(input: TextInput):
    result = nlp_sentiment(input.text)
    return {"prediction": result}

@app.post("/ask/")
def ask(input: QuestionOnlyInput):
    # Generate an answer based on the question without context
    result = nlp_chatgpt(input.question, max_length=150, num_return_sequences=1, temperature=0.7, top_k=50)
    return {"answer": result[0]['generated_text'].strip()}
