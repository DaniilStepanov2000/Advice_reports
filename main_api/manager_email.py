import logging
import smtplib
from django.conf import settings
from django.http import HttpRequest
from django.db.models import QuerySet
from main_api.models import Report
from email.mime.text import MIMEText


logger = logging.getLogger('django')


class EmailManager:
    @staticmethod
    def send_email(recv_email: str, message: str) -> None:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(settings.EMAIL_SENDER, settings.EMAIL_KEY)

        msg = MIMEText(message)
        msg['Subject'] = 'Daily advice'
        msg['To'] = recv_email
        msg['From'] = settings.EMAIL_SENDER

        s.sendmail(settings.EMAIL_SENDER, recv_email, msg.as_string())
        logger.info(f'Send email to {recv_email} with message {message}')
        s.quit()


class ScheduleManager:
    def __init__(self, request: HttpRequest):
        self.request = request

    def create_schedule(self) -> None:
        """
        Create schedule reports in database with passed parameters
        """
        new_report = Report.objects.create(
            owner=self.request.user,
            time=self.request.POST['schedule_time']
        )
        new_report.save()
        logger.info(f'Created new report: {new_report}')

    def delete_schedule(self) -> None:
        """
        Delete schedule reports from database
        """
        report = Report.objects.get(
            owner=self.request.user,
            id=self.request.POST['delete_report_id']
        )
        report.delete()

    def get_reports(self) -> QuerySet:
        """
        Get all reports for user
        """
        reports = Report.objects.filter(owner=self.request.user)
        return reports


