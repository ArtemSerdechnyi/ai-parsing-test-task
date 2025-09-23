import asyncio

from celery.result import AsyncResult
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from dependency_injector.wiring import Provide, inject

from app.file.domain.enums import ProcessStatus
from celery_task import celery_app

ws_router = APIRouter()


@ws_router.websocket("/ws/file-processing/task/{task_id}/status")
@inject
async def websocket_verify(
    websocket: WebSocket,
    task_id: str,
):
    await websocket.accept()
    last_status = None
    try:
        while True:
            result = AsyncResult(task_id, app=celery_app)
            meta = result.info if result.info else {}
            current_status = meta.get("status", "")

            if current_status != last_status:
                await websocket.send_json({
                    "status": current_status,
                })
                last_status = current_status
                continue

            await asyncio.sleep(0.1)

            if result.status in ("SUCCESS", "FAILURE"):
                break
    except WebSocketDisconnect:
        print("Ws error")
    finally:
        if last_status != ProcessStatus.COMPLETED:
            await websocket.send_json({
                "status": ProcessStatus.COMPLETED,
            })

        await websocket.close()
        print("Ws closed")
