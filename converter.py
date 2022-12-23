import ffmpeg



# Cria o objeto de entrada usando o caminho para o arquivo de entrada
input_audio = ffmpeg.input("whatsapp.opus")

# Cria o objeto de saída usando o objeto de entrada e o caminho para o arquivo de saída
# Especifica o codec de áudio como "pcm_s16le" para gerar um arquivo WAV
output_audio = input_audio.output("output.wav", acodec="pcm_s16le")

# Executa a conversão usando o objeto de saída
ffmpeg.run(output_audio)