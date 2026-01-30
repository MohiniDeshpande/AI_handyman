class Session:
    def __init__(self):
        self.audio_b64 = None
        self.image_b64 = None

    def set_audio(self, b64: str):
        self.audio_b64 = b64

    def set_image(self, b64: str):
        self.image_b64 = b64

    def build_payload(self) -> dict:
        payload = {"type": "input"}

        if self.audio_b64:
            payload["audio"] = {
                "mime_type": "audio/pcm;rate=16000",
                "data": self.audio_b64
            }

        if self.image_b64:
            payload["image"] = {
                "mime_type": "image/jpeg",
                "data": self.image_b64
            }

        return payload
