from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from dependency_injector.wiring import Provide, inject

ws_router = APIRouter()

@ws_router.websocket("/ws/test")
@inject
async def websocket_verify(
    websocket: WebSocket,
):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            await websocket.send_json({"status": "ok"})
    except WebSocketDisconnect:
        print("Ws error")


@ws_router.get('/test/get')
async def get_test():
    return {"status": "ok"}
