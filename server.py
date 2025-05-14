from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from ai_core import generate_optimistic_response
import asyncio

app = FastAPI()
active_connections = []

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            response = generate_optimistic_response(data)
            for conn in active_connections:
                await conn.send_text(f"Solis: {response}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)