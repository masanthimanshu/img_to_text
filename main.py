from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "It's Working!!"}

@app.get("/image/{img_name}")
def read_root(img_name):
    img_to_txt = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    text = img_to_txt(f"https://images.unsplash.com/{img_name}")

    return text
