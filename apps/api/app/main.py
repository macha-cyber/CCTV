from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = set()


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)

    try:
        while True:
            await websocket.receive_text()
    except:
        clients.remove(websocket)


@app.post("/event")
async def event(payload: dict):

    # 全クライアントへ通知
    dead = []

    for c in clients:
        try:
            await c.send_json(payload)
        except:
            dead.append(c)

    for d in dead:
        clients.discard(d)

    return {"status": "ok"}