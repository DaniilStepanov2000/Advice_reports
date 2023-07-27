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
4. Run docker
   
