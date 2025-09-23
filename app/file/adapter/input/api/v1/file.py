import uuid

from fastapi import APIRouter, File, UploadFile, HTTPException, Depends

from celery_task.tasks.parse_file import ProcessFilesTask, get_process_files_task
from core.config import config

file_router = APIRouter()


@file_router.post("/upload-files")
async def upload_files(
    abm_file: UploadFile = File(...),
    sup_file: UploadFile = File(...),
    process_files_task: ProcessFilesTask = Depends(get_process_files_task)
):
    upload_dir = config.UPLOADED_FILES_DIRECTORY

    try:
        abm_path = upload_dir / f"{uuid.uuid4()}_{abm_file.filename}"
        with open(abm_path, "wb") as f:
            content = await abm_file.read()
            f.write(content)

        sup_path = upload_dir / f"{uuid.uuid4()}_{sup_file.filename}"
        with open(sup_path, "wb") as f:
            content = await sup_file.read()
            f.write(content)

        task = process_files_task.delay(abm_path=str(abm_path), sup_path=str(sup_path))

        # try:
        #     res = process_files(abm_path=str(abm_path), sup_path=str(sup_path))
        # except Exception as e:
        #     import traceback
        #     traceback.print_exc()
        #     print(e)
        #     raise

        return {"abm_file": str(abm_path), "sup_file": str(sup_path), "task_id": task.id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload files: {e}")
