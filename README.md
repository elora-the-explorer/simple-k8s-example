# depop-k8s-example
Depop interview example

Preparation before your interview: We would like you to prepare a small example setup ahead of the interview - This does not need to be a fully implemented and complex solution - We're looking to discuss your thought process behind your decisions, and can solve the issue together during the interview.

* A running kubernetes cluster (can be minikube, equivalent or online)

* A repository with a deployable application (can be very minimal)

* A deployment process of some form to build and deploy that application to that cluster (this could be local or using a CICD system)

Just to confirm, this can be as simple or as complex as you wish - and doesn't need to work in full at time of the interview. Feel free to put together what you're most comfortable with, in the time you have.

#### The API 
This app provides a very simple api for greeting the user based on a provided language. It supports English, Maori, Dutch, and French. 

```
GET /greet/<language>
```

example
```
GET /greet/maori
Kia Ora!
```

kubectl apply -f kubernetes/deployment.yaml
### Run the flask app locally (Windows 10)
All instructions assume you are in the root directory of the project. 

### Pre-requisites 
* Python 3.9 
* Docker Desktop (with K8s enabled)
* Kubectl set up with the docker-desktop context
* Make


#### Install Dependencies
```
make init
```

#### Run app locally
```
make app
```

### Run Unit Tests 

```
make test
```

### Run App in Docker 
You'll need to have Docker Desktop running for this step

```
make docker-up
```

You should how be able to access the app at localhost:5001

### Deploy App to K8s
You'll need to have Kubernetes enabled in Docker Desktop and Kubectl set up with the docker-desktop context for this step

```
make deploy
```



