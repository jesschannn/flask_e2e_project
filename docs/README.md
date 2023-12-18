# flask_e2e_project

# Overview
This repository is my HHA 504 Final Project, which contains code that allows users to view data about medical malpractice statistics displayed on a web application, as well as educate users on what medical malpractice is. 

# Technologies Utilized
Technologies used were Flask, Tailwind, MySQL Database on Azure, SQLAlchemy, API service via Flask, Google OAuth, Sentry,io, Docker, and Azure. 

- Flask: web development (backend)
- Tailwind: front-end styling
- MySQL Database on Azure: data storage
- SQLAlchemy: database interaction
- Google OAuth: authorization
- Sentry.io: error monitoring
- Docker: containerization
- Azure: deployment

# Deployment Steps

## How to Run Without Docker Locally

If an individual wanted to run my code locally without Docker, they would have to clone my app.py, templates folder, requirements.txt, .env, .gitignore, static folder, and oauth folder (everything in the app folder). Then the individual would have to `cd` into their on workspace, `cd` into the app folder, and run `python app.py` in their console. 

![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/c23e5a0d-d591-4f46-ab5e-e69b89de59ad)

## How to Run With Docker Locally

If an individual wanted to run my code locally with Docker: 
1. Clone my entire app folder.
2. Create a Docker file with the following lines:

```
FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```
   
3. Docker build: ```docker build -t <name>```
4. View the image: ```docker images```
5. Run Docker: ```docker run -d -p <port you want to run it on>:<port exposed> <name>```
6. Display information about Docker containers: ```docker ps```
7. Stop the Docker image from running: ```docker stop <container id>```
8. Delete Docker image: ```docker system prune -a -f```

![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/3531d510-ae8a-4f51-89ed-333037a7b35a)


## How to Deploy to Cloud
If an individual want to deploy my code onto the Cloud:
1. Install Azure CLI: ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```
2. Log in: ``az login --use-device-code```
3. Create a resource group: ```az group create --name <name of resource group> --location eastus```
4. Deploy the Azure App Service: ```az webapp up --name <name of app service> --sku B1 --runtime "PYTHON | 3.9" --resource-group <resource group name>```
5. Click on the link provided in the console

![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/1ab38566-db97-46b3-8386-de228cd994d5)

# Template of the .env File

```
DB_URL= ***
DB_HOST= ***
DB_DATABASE= ***
DB_USERNAME= ***
DB_PASSWORD= ***
DB_PORT= ***
DB_CHARSET= ***

GOOGLE_CLIENT_ID= ***
GOOGLE_CLIENT_SECRET= ***
```

# Screenshots

## Screenshots of Web Application (Local)

![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/09d28673-7a43-4095-ab67-b5dc67498f3c)
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/5138f420-2ec9-490e-bfae-850be956a5fb)
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/1823aa44-49e6-46aa-a10f-0cdbef9f9391)
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/89188fac-20a9-42e0-bba8-2d4434de683c)

## Screenshots of Google OAuth
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/e65ad256-940b-41c1-a386-505689416fbb)
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/62136645-da65-4cc6-a3b5-d36a44773e6e)

## Screenshot of SQL Workbench
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/0cdfe105-489f-459b-8aa3-069a078f94f2)

## Screenshot of SQL Database - Azure
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/4c1e58a5-45b8-4b5f-9345-cdf20fb07cf6)

## Screenshot of API Endpoint
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/db2fa2cb-aadb-4508-a6e0-dc6da98d64fb)

## Screenshot of Error Endpoint
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/b063b5b6-e97d-478d-b5a1-a69904b7f510)

## Screenshot of Sentry.io
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/de35f3bc-1375-4fb0-aa5f-911fc592ec1d)

## Screenshot of Docker
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/598492ab-a367-45d8-8a30-28faa78b5e4e)

## Screenshot of Azure Deployment
![image](https://github.com/jesschannn/flask_e2e_project/assets/123782059/6e75e053-f086-47fe-b5ca-fdcc3afcf2e4)
