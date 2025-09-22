import abc

from celery import Task, Celery
from celery.result import AsyncResult


class CeleryTaskBase(abc.ABC):
    celery_app: Celery

    def __init__(self, celery_app: Celery):
        self.celery_app = celery_app

    def delay(self, *args, **kwargs) -> AsyncResult:
        return self._task.delay(*args, **kwargs)

    @property
    @abc.abstractmethod
    def _task(self) -> Task:
        raise NotImplementedError
