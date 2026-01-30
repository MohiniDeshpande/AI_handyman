import os

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

GEMINI_WS_URL = (
    "wss://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-live:stream"
)

AUDIO_MIME = "audio/pcm;rate=16000"
IMAGE_MIME = "image/jpeg"
