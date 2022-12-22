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
    print(filename)
    extension = file.filename.split(".")[1]
    if extension == 'wav' or extension == 'mp3':
        with open(filename, "wb") as f:
            contents = await file.read()
            f.write(contents)
            r = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                audioStored = r.record(source)
                print('gravando audio original')
                audio = AudioSegment.from_file(audioStored, format="mp3")
                print('Convertendo para WAV')
                audio.export("output.wav", format="wav")
                #text = r.recognize_google("output.wav", language='pt-BR')
                #return text
    else:
        raise HTTPException(status_code=500, detail='Formato não aceito no momento, tente com .wav ou .mp3')
