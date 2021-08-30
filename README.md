## Simple App 
This repoisotiry provides a very simple API for greeting the user based on a provided language. It supports English, Maori, Dutch, and French. 

```
GET /greet
GET /greet/<language>
```

example
```
GET /greet/maori
Kia Ora!
```

## Run Simple App locally (Windows 10)
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

You should how be able to access the app at localhost:5001.
You can execute the deployment tests against the docker container with the following command. 
```
make docker-test
```

### Deploy App to K8s
You'll need to have Kubernetes enabled in Docker Desktop and Kubectl set up with the docker-desktop context for this step

```
make deploy
```

This will perform the following actions
* Execute the project unit tests
* Build the docker image 
* Deploy two replicas of the app to k8s and make it accessible via a service listening on port 8080. 
* Execute a simple deployment test to check that the app is running correctly 

You should now be able to access the app at localhost:8080

When you're down, run the following command to tear the everything down

```
make tear-down
```



