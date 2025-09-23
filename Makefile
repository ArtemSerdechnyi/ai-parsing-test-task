.PHONY: up cov test celery migrate run

cov:
	coverage run -m pytest
	coverage html

test:
	ENV=test pytest tests -s

up:
	docker-compose -f docker/docker-compose.yml up

celery:
	celery -A celery_task.celery_app worker --loglevel=INFO

migrate:
	alembic upgrade head

run:
	python3 main.py --env local --debug
