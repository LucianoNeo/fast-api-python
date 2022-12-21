from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4 as uuid
import speech_recognition as sr
from pydub import AudioSegment

class SaleModel(BaseModel):
    id: Optional[str]
    name: str
    price: float = Field(
        gt=0, description="The price must be greater than zero")
    quantity: int = Field(
        gt=0, description="The quantity must be greater than zero")


app = FastAPI()

sales = [
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2e",
        "name": "notebook",
        "price": 500,
        "quantity": 3
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2f",
        "name": "iphone",
        "price": 700,
        "quantity": 1
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2g",
        "name": "monitor",
        "price": 200,
        "quantity": 3
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2h",
        "name": "keyboard",
        "price": 10,
        "quantity": 6
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2i",
        "name": "mouse",
        "price": 10,
        "quantity": 5
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2j",
        "name": "webcam",
        "price": 20,
        "quantity": 2
    }
]


@app.get('/')
def home():
    return {"message": "Welcome to Neo's audio transcription's API!"}

@app.post("/uploadaudio/")
async def create_upload_audio(audio: bytes = File(...)):
    #extension = audio.filename.split(".")[1]
    #if extension == 'wav' or extension == 'mp3':
        with open("audio.wav", "wb") as f:
            f.write(audio)
            r = sr.Recognizer()
            with sr.AudioFile('audio.wav') as source:
                audioStored = r.record(source)
                text = r.recognize_google(audioStored, language='pt-BR')
        return text
