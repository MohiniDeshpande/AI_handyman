import base64
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from app.session import Session
from app.gemini_ws import GeminiLiveClient

app = FastAPI()


@app.websocket("/ws/spectacles")
async def spectacles_ws(ws: WebSocket):
    await ws.accept()

    session = Session()
    gemini = GeminiLiveClient()
    await gemini.connect()

    try:
        while True:
            msg = await ws.receive()

            # Control message (JSON)
            if msg.get("text"):
                control = json.loads(msg["text"])
                session.last_type = control["type"]

            # Binary frame
            elif msg.get("bytes"):
                b64 = base64.b64encode(msg["bytes"]).decode()

                if session.last_type == "audio":
                    session.set_audio(b64)
                elif session.last_type == "video":
                    session.set_image(b64)

                payload = session.build_payload()
                await gemini.send(payload)

                response = await gemini.receive()
                await ws.send_json(response)

    except WebSocketDisconnect:
        pass
    finally:
        await gemini.close()

