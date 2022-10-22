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

![Picture5](https://user-images.githubusercontent.com/108364254/197350483-81a33653-ac9c-4ce1-87f6-19bec93ef1b1.png)


