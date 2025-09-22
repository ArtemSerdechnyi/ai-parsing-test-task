import uuid

from fastapi import APIRouter, File, UploadFile, HTTPException

from core.config import config

file_router = APIRouter()


@file_router.post("/upload-files")
async def upload_files(
    abm_file: UploadFile = File(...),
    sup_file: UploadFile = File(...),
):
    upload_dir = config.UPLOADED_FILES_DIRECTORY

    try:
        abm_path = upload_dir / f"{abm_file.filename}_{uuid.uuid4()}"
        with open(abm_path, "wb") as f:
            content = await abm_file.read()
            f.write(content)

        sup_path = upload_dir / f"{sup_file.filename}_{uuid.uuid4()}"
        with open(sup_path, "wb") as f:
            content = await sup_file.read()
            f.write(content)

        return {"abm_file": str(abm_path), "sup_file": str(sup_path)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload files: {e}")
