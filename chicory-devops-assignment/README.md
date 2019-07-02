## Chicory Devops Home Assignment

You are tasked with deploying this respository to Kubernetes.

### Project Description
This repository provides an endpoint that echoes a counter value in Redis. Each time that a user hits the endpoint, the number increments. The endpoint is accessible at  /test_view/. 

The project is written using Python 3 and the Django framework. You may use Minikube and Redis 3.2.4 and up.

### Network Services
This repository requires a working Redis deployment.

### Home Assignment

You are to create the required configuration and deployment settings for Kubernetes and Docker. 

* You may find the Django project configuration in chicory-devops-assignment/settings.py
* You may find the Python dependencies in the requirements.txt file.
* In order to start the Django server execute the following command: ```./manage.py runserver```

Deliverables include:

1. Dockerfile
2. Kubernetes deployment file
3. Kubernetes service file 
4. Step-by-step instructions on how to deploy the code

Archive your solution and attach it to an email to <dev@chicory.co>. Please feel free to reach out if you have any questions. Good luck!

