import datetime
from zoneinfo import ZoneInfo
from dateutil import parser
from schedule_reports_email.celery import app
from .models import Report
from .manager_email import EmailManager
from .manager_data import DataManager
import logging

logger = logging.getLogger('django')

app.conf.beat_schedule = {
    'check_schedule_every_minutes': {
        'task': 'main_api.tasks.generate_tasks',
        'schedule': 60.0,

    },
}


def check_time(report_time):
    convert_time = parser.parse(str(report_time))
    current_time = datetime.datetime.now(ZoneInfo("Europe/Moscow"))
    logger.info(f'Current time: {current_time}')
    return convert_time.hour == current_time.hour and convert_time.minute == current_time.minute


@app.task
def generate_tasks():
    for report in Report.objects.all():
        if check_time(report.time):
            message = DataManager().get_data()
            logger.info(f'generate_tasks: Get the following data: {message}')
            EmailManager.send_email(report.owner.email, message)
