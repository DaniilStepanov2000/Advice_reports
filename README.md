# Advice report system
## Project
This system developed for people hwo want to send reminders with some "wise advice" to an email. 
## Technical details
Currently, the system can send emails by any time using the scheduler. Thanks to the Celery especially for the celery beat and the message broker RabbitMQ, system can perform asynchronous tasks because we don't want to block main proccess.
### Technical stack:
1. Python 3.11.
2. Django.
3. Celery.
4. RabbitMQ.
5. Docker.
6. SQLite.
7. PyTest.
### Deploy system:
1. Clone the following [repository](https://github.com/DaniilStepanov2000/Advice_reports) to your machine.
2. Make the following command to go to the root project folder:
```
cd advice_reports
```
3. Install and setup Docker.
4. Run the following command to build the app image:
```
docker build . -f Docker/. -t schedule_email
```
5. Run the following command to start the containers:
```
docker-compose -f Docker/docker-compose.yml up
```
6. Enter the following address in the your browser:
```
0.0.0.0:8000
```
### Run unit-test
To run tests all unit-tests go to the root folder of project and run the following command:
```
pytest
```
