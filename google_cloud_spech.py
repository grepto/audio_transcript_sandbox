from envparse import env
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

env.read_envfile()

def transcribe_stream(stream: bytes) -> str:
    """Transcribe the given audio stream asynchronously."""

    client = speech.SpeechClient()

    audio = types.RecognitionAudio(content=stream)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=16000,
        language_code='ru-RU')

    transcription = client.long_running_recognize(config, audio)
    response = transcription.result(timeout=90)
    res = [result.alternatives[0].transcript for result in response.results]
    return ' '.join(res)
