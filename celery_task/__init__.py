from celery import Celery

from celery_task.tasks.parse_file import process_files_task
from core.config import config

celery_app = Celery(
    "worker",
    backend=config.CELERY_BACKEND_URL,
    broker=config.CELERY_BROKER_URL,
)

celery_app.conf.task_routes = {"worker.celery_worker.test_celery": "test-queue"}
celery_app.conf.update(task_track_started=True)
celery_app.autodiscover_tasks()
