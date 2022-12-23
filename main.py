import speech_recognition as sr
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
import ffmpeg
import datetime
import os

original_path = '/data/original'
converted_path = '/data/converted'

if not os.path.exists(original_path):
    os.makedirs(original_path)

if not os.path.exists(converted_path):
    os.makedirs(converted_path)

app = FastAPI()
AZURE_SPEECH_KEY = os.environ.get("AZURE_SPEECH_KEY")

@app.get('/')
def home():
    return {"message": "Welcome to Neo's audio transcription's API!"}

@app.post("/uploadaudio/")
async def create_upload_audio(file: UploadFile):
    now = datetime.datetime.now()
    dateFormated = now.strftime("-%d-%m-%Y-%H-%M-%S")
    filename = str(file.filename.split(".")[0] + dateFormated + "." + file.filename.split(".")[1])
    filenameStore = os.path.join(original_path,filename)
    extension = file.filename.split(".")[1]

    if extension != 'wav':
        with open(filenameStore, "wb") as f:
            contents = await file.read()
            f.write(contents)
            outputFileName = str(filename.split(".")[0] + "-converted"+".wav")
            outputFileNameStore = os.path.join(converted_path, outputFileName)
            input_audio = ffmpeg.input(filenameStore)
            output_audio = input_audio.output(outputFileNameStore, acodec="pcm_s16le")
            ffmpeg.run(output_audio,overwrite_output=True)        
            r = sr.Recognizer()
            with sr.AudioFile(outputFileNameStore) as source:
                audioStored = r.record(source)
                transcription = r.recognize_azure(audioStored, key=AZURE_SPEECH_KEY,location="eastus",language="pt-BR")
                result = transcription[0]
            return result
    else:
        with open(filenameStore, "wb") as f:
            contents = await file.read()
            f.write(contents)        
            r = sr.Recognizer()
            with sr.AudioFile(filenameStore) as source:
                audioStored = r.record(source)
                transcription = r.recognize_azure(audioStored, key=AZURE_SPEECH_KEY,location="eastus",language="pt-BR")
                result = transcription[0]
            return result
