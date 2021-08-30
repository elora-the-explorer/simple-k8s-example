init: 
	pip install -r flask-app/requirements.txt && \
	pip install pytest
	pip install requests

app: 
	export FLASK_APP=flask-app/simple_app && \
	export FLASK_ENV=development && \
	python -m flask run

test: 
	cd flask-app && python -m pytest

docker-build: 
	docker build -f docker/Dockerfile -t simple-app:latest .

docker-up: docker-build
	docker run -p 5001:5000 simple-app

deploy: test docker-build
	kubectl apply -f kubernetes/deployment.yaml && \
	cd deployment-test && python -m pytest --url http://localhost:8080

tear-down: 
	kubectl delete -f kubernetes/deployment.yaml




	
	





