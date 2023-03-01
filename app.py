from fastapi import FastAPI, Request, Response
from pydantic import BaseModel, validator
import time
import asyncio

from ml import extract_keywords 

class Text(BaseModel):
    text: str
    

class Textlist(BaseModel):
    articles: list(Text)
    
    @validator("articles", pre=True, each_item=True)
    def each_item_should_be_a_string(cls, articles):
        if not all(isinstance(article, str) for article in articles):
            raise ValueError(f"All articles should be of type string")
        return articles
    
class TextRequest(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world again"}


@app.post("/keywords")
async def generate_keywords(request: Request, text: TextRequest):
    keywords = extract_keywords(text.text)
    return{"keywords": keywords}

