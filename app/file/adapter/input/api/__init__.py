from fastapi import APIRouter

from app.file.adapter.input.api.v1.websocket import ws_router as ws_v1_router
from app.file.adapter.input.api.v1.file import file_router as file_v1_router

router = APIRouter()
router.include_router(ws_v1_router, prefix="/api/v1/file", tags=["File"])
router.include_router(file_v1_router, prefix="/api/v1/file", tags=["File"])

__all__ = ["router"]
