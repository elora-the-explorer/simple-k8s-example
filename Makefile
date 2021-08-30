init: 
	pip install -r flask-app/requirements.txt && \
	pip install pytest

app: 
	export FLASK_APP=flask-app/simple_app && \
	export FLASK_ENV=development && \
	python -m flask run

test: 
	python -m pytest

docker-up:
	docker build -f docker/Dockerfile -t simple-app:latest . && \
	docker run -p 5001:5000 simple-app

	

