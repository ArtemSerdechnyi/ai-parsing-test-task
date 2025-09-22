.PHONY: up

cov:
	coverage run -m pytest
	coverage html

test:
	ENV=test pytest tests -s

up:
	docker-compose -f docker/docker-compose.yml up
