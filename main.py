import speech_recognition as sr
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from pydub import AudioSegment

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Welcome to Neo's audio transcription's API!"}

@app.post("/uploadaudio/")
async def create_upload_audio(file: UploadFile):
    filename = file.filename
    extension = file.filename.split(".")[1]
    if extension == 'wav' or extension == 'mp3':
        with open(filename, "wb") as f:
            contents = await file.read()
            f.write(contents)
            r = sr.Recognizer()
            audio = AudioSegment.from_file(filename, format="mp3")
            audio.export("output.wav", format="wav")
            with sr.AudioFile("output.wav") as source:
                audioStored = r.record(source)
                
                text = r.recognize_google(audioStored, language='pt-BR')
                return text
    else:
        raise HTTPException(status_code=500, detail='Formato não aceito no momento, tente com .wav ou .mp3')
