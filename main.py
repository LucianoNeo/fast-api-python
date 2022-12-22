import speech_recognition as sr
from fastapi import FastAPI, File, Form, HTTPException, UploadFile

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Welcome to Neo's audio transcription's API!"}

@app.post("/uploadaudio/")
async def create_upload_audio(file: UploadFile):
    filename = file.filename
    extension = file.filename.split(".")[1]
    if extension == 'wav':
        with open(filename, "wb") as f:
            contents = await file.read()
            f.write(contents)
            r = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                audioStored = r.record(source)
                text = r.recognize_google(audioStored, language='pt-BR')
                return text
    else:
        raise HTTPException(status_code=500, detail='Formato não aceito no momento, tente com .wav')
