# Advice report system
## Project
This system developed for people hwo want to send reminders with some "wise advice" to an email. 
## Technical details
Currently, the system can send emails by any time using scheduler. Thanks to the Celery especially for the celery beat and message broker RabbitMQ, system can perform asynchronous tasks because we don't want to block main proccess.
### Technical stack:
1. Python 3.11.
2. Django.
3. Celery.
4. RabbitMQ.
5. Docker.
6. SQLite.
7. PyTest.
### Deploy system:
1. Clone the following [repository](https://github.com/DaniilStepanov2000/advice_reports) to your machine.
2. Make the following command to go to the root project folder:
```
cd advice_reports
```
3. Install and set-up Docker.
4. Run the following command to build app image:
```
docker build . -f Docker/. -t schedule_email
```
5. Run the following command to start containers:
```
docker-compose -f Docker/docker-compose.yml up
```
6. Run the following command to connect to the app container
```
docker exec -it container_id /bin/bash
```
7. Run the following command to start celery beat.
```
celery -A schedule_reports worker -B
```
### Run unit-test
To run tests all unit-tests go to the root folder of project and run the following command:
```
pytest
```
