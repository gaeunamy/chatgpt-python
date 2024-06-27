from openai import OpenAI
client = OpenAI()

file = open("sample.wav", "rb")
transcript = client.audio.transcriptions.create (
    model="whisper-1",
    file=file,
    response_format="srt"
)

print(transcript)