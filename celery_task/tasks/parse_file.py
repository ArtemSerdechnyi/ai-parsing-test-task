from celery import shared_task

from app.file.domain.file_processing import process_files as _process_files


@shared_task(name="worker.celery_worker.process_files")
def process_files_task(abm_path: str, sup_path: str):
    return _process_files(abm_path, sup_path)
