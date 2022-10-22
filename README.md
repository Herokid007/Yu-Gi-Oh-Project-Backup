# Yu-Gi-Oh-Project

## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The App](#The-App)
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## The Project Brief  
The aim for the project was to design a web application intergrated with a database via Python using Flask micro-framework. The design for the app needed to have a CRUD functionality (create, read, update, and delete). The CI/CD pipeline creates the automation via Jenkins deployment, then the app is deployed using Docker products (Dockerfile, Docker-Compose, & Docker-Swarm) interfaced using Microsoft Azure VMs. The information is stored via a MySQL database consisting of two tables and sharing a one-to-many relationship.

![Picture2](https://user-images.githubusercontent.com/108364254/197344567-b0a8d54c-a732-48ad-b06a-b83d60f54d55.png)

The diagram illusrates the basic premise of the web app functionality. The HTML will acts as the front-end interfaced with the Flask micro-framework via Python to execute the logic and the information is stored via MySQL database, both the micro-framework and database acts as the back-end server. 

## The App Design
In terms of the design I have chosen to build a Yu-Gi-Oh! database app, which allows users to enter their favourite duel monster card and the monster type (create function), view the new data via the index.html page (read function), users can also update the current data, i.e. the ID of the duel monster card is linked to the card name and type (update function), additionally the user can also delete the current data relative to the card ID (delete function). The database for this project consists of a duel monster name table and an duel monster type table, hence with each duel monster type is associated with multiple duel monster names (one-to-many relationship). The Entity Relationship Diagram is illustrated below:

![Picture6](https://user-images.githubusercontent.com/108364254/197350597-fbe5e13e-a0be-4dcc-97a8-081a5e7dc5ac.png)

The ERD diagram illustrates the functionality of the MySQL database. The foreign key is assiocated with the duel monster name and level, where card ID will be linked via both the name and type relationship.

## The CI/CD Pipeline 
The project required the implementation of several stages of a automated CI/CD pipeline. These included: versiom control, development enviroment and an build server.

<INSERT IMAGE HERE>

Github was used for version control the project respository hosted via Github.com. In terms of version control via Github this allows updates to the project to be commited and pushed, whilst keeping the commit history for access to previous versions. The Github as a repository allows the repository to host the service and to be stored via the development enviroment, in addition providing webhooks, which sends HTTP POST requests to the build server to automate both the build and the unit-testing.
  
The development environment used was Python3 virtual environment (venv) hosted on a virtual machine running Ubuntu 20.04. Python is used as the core for the code and the Flask is a python-based micro-framework. The venv allows the pip to install the basic requirements.txt and the performance of the app to run without causing any conflicts when pip install the modules on the same machine or VMs.

Jenkins will be used as the build server to provide the automation for both the build and the unit-testing. It is to note the automation is achieved by setting up a freestyle project, which will execute the test.sh script when it recieves the webhook via Github (files needs to commited then pushed). Jenkins will also be used to run the app via Gunicorn, achieved when testing is completed.

<INSERT IMAGE HERE>
  
 ## The Risk Assessment

