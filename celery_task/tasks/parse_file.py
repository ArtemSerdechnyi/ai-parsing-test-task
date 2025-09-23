from celery import shared_task, Task

from app.file.domain.file_processing import process_files as _process_files


@shared_task(name="worker.celery_worker.process_files", bind=True)
def process_files_task(self: Task, abm_path: str, sup_path: str):
    return _process_files(self, abm_path, sup_path)
