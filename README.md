# RESTfulWebService-using-Docker

Steps for running the application in a docker container:

Note- Please ensure you have docker installed on your system. If not, visit https://docs.docker.com/engine/installation/

1. Clone the repository
2. Build a new docker image using the following command:
   sudo docker build -t <myimagename> .
3. Execute the app using the following command:
   sudo docker run -p <port>:80 <myimagename>



