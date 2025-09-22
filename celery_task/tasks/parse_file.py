from pathlib import Path

from celery_task import celery_app
from celery_task.tasks import CeleryTaskBase


class ProcessFilesTask(CeleryTaskBase):

    @property
    def _task(self):

        @self.celery_app.task(name="worker.celery_worker.process_files")
        def process_files(abm_path: str, sup_path: str):
            abm_path = Path(abm_path)
            sup_path = Path(sup_path)

            searched_columns_names = ["company_name", "domain_name"]



            return {"status": "done", "abm_file": abm_path, "sup_file": sup_path}

        return process_files

def get_process_files_task() -> ProcessFilesTask:
    return ProcessFilesTask(celery_app)

# @celery_app.task(name="worker.celery_worker.process_files")
# def process_files(abm_path: str, sup_path: str):
#     abm_path = Path(abm_path)
#     sup_path = Path(sup_path)
#
#
#     return {"status": "done", "abm_file": abm_path, "sup_file": sup_path}
