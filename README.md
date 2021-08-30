# depop-k8s-example
Depop interview example

Preparation before your interview: We would like you to prepare a small example setup ahead of the interview - This does not need to be a fully implemented and complex solution - We're looking to discuss your thought process behind your decisions, and can solve the issue together during the interview.

* A running kubernetes cluster (can be minikube, equivalent or online)

* A repository with a deployable application (can be very minimal)

* A deployment process of some form to build and deploy that application to that cluster (this could be local or using a CICD system)

Just to confirm, this can be as simple or as complex as you wish - and doesn't need to work in full at time of the interview. Feel free to put together what you're most comfortable with, in the time you have.

### Run the flask app locally (Windows 10)
All instructions assume you are in the root directory of the project. 

#### Install Flask
```
pip install Flask
```

#### Export environment variables
```
export FLASK_APP=flask-app/simple_app
export FLASK_ENV=development
```

#### Run Flask 
```
python -m flask run
```

#### Run Tests 

```
pip install pytest
python -m pytest
```

#### The API 
This app provides a very simple api for greeting the user based on the provided language. It supports English, Maori, Dutch, and French. 

```
GET /greet/<language>
```

example
```
GET /greet/maori
Kia Ora! 
```
