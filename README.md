# Sentiment classification App

## Table of Contents

- [Sentiment classification App](#sentiment-classification-app)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation and Application Startup](#installation-and-application-startup)
  - [Usage](#usage)


## Description

This sentiment classification application features a DistilBERT model that has undergone fine-tuning on a targeted subset of Amazon product reviews, with a specific focus on Amazon appliance reviews. The application's core purpose is to operate as an internal tool and API, proficiently discerning critical negative sentiments within product reviews. Subsequent to identification, these reviews are designated for comprehensive analysis by human evaluators.

The backend is developed using FASTAPI which interacts with a MySQL database using SQlAlchemy. The database is used to manage the user interactions, store the text classification requests and the response of the model, so that a human may review them in the future. A simple reactjs based frontend is also developed for demonstrative and testing purposes.

More information about the fine-tuned HuggingFace model can be viewed **[here](https://huggingface.co/m-aamir95/finetuning-sentiment-classification-model-with-amazon-appliances-data)**

To make deployment easier and smooth, docker has been employed which hosts the following three containers.

1. FastAPI based backend container.
2. ReactJS based frontend container.
3. MySQL database container.


## Installation and Application Startup

To get started with the Project, follow these steps:

1. Clone the repository: `git clone [repository link]`
2. Navigate to the project directory: `cd fastapi-ml-service`
3. Install the linux dependencies including docker: `sudo bash bash_scripts/install_system_dependencies.sh`
4. Currently we need to manually create the `sentiment_db` inside the mysql docker container (Ideally it should be a part of post container init script). Following are the steps to manually create the `sentiment_db` inside the mysql container.
   *  sudo docker-compose up --build -d db
   *  sudo docker exec -it db bash # Jump into the db container
   *  mysql -u root -p
   *  When prompted enter the mysql root password which is by default set to `my-secret-pw`
   *  create database sentiment_db;
   *  exit # Exit MySQL shell
   *  exit # Exit container
5. Start all the containers `sudo docker-compose up -d --build`
6. The FastAPI is hosted at `PORT 8080` and the ReactJS based frontend is hosted at `PORT 80`
7. Nagivate to `http://localhost:80`

## Usage

1. The FastAPI API points can be viewed by visiting http://localhost:8080/docs
2. 
3. You can also interact with the app by visiting http://localhost:80 