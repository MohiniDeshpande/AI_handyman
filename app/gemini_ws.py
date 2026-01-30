import json
import websockets
from app.config import GEMINI_API_KEY, GEMINI_WS_URL


class GeminiLiveClient:
    async def connect(self):
        self.ws = await websockets.connect(
            GEMINI_WS_URL,
            extra_headers={
                "Authorization": f"Bearer {GEMINI_API_KEY}",
                "Content-Type": "application/json"
            }
        )

        # CRITICAL SYSTEM PROMPT
        await self.send({
            "type": "setup",
            "system_instruction": (
                "You are a real-time AI handyman assistant.\n"
                "Use audio and video together.\n"
                "If the video is unclear or insufficient, respond with:\n"
                "{ \"request\": \"better_view\", \"text\": \"<explanation>\" }\n"
                "If the task is dangerous, include:\n"
                "{ \"warning\": true }\n"
                "Otherwise give step-by-step instructions."
            )
        })

    async def send(self, payload: dict):
        await self.ws.send(json.dumps(payload))

    async def receive(self) -> dict:
        return json.loads(await self.ws.recv())

    async def close(self):
        await self.ws.close()