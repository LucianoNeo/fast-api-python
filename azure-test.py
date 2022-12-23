import os
import time
import azure.cognitiveservices.speech as speechsdk
import sys

service_region = "eastus"

speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)
speech_config.speech_recognition_language="pt-BR"

audio_config = speechsdk.audio.AudioConfig(filename="audio2.wav")

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

done = False

def stop_cb(evt):
        print('Arquivo transcrito com sucesso!')
        speech_recognizer.stop_continuous_recognition()
        global done
        done = True
def recognized_cb(evt):
    # Abra o arquivo de transcrição para escrita
    with open("transcription.txt", "w") as f:
        # Escreva o texto da transcrição no arquivo
        f.write(evt.result.text)


speech_recognizer.recognizing.connect(lambda evt: print(''))
speech_recognizer.recognized.connect(recognized_cb)
speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED '))
speech_recognizer.canceled.connect(lambda evt: print('CANCELED '))

speech_recognizer.session_stopped.connect(stop_cb)
speech_recognizer.canceled.connect(stop_cb)

speech_recognizer.start_continuous_recognition()

while not done:
    time.sleep(.5)

