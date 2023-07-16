import pytest
from django.contrib.auth.models import User
from main_api.models import Report

from main_api.manager_email import ScheduleManager


@pytest.mark.django_db
def test_create_schedule(user_factory, request_factory):
    user = user_factory(username='some_user', password='some_password', email='test')
    prepared_request = request_factory(user, schedule_time='10:29')

    ScheduleManager(prepared_request).create_schedule()

    assert User.objects.count() == 1
    assert Report.objects.count() == 1


@pytest.mark.django_db
def test_delete_schedule(report_factory, user_factory, request_factory):
    user = user_factory(username='test_user', password='test', email='test')
    report = report_factory(time='10:29', owner=user)
    prepared_request = request_factory(user, schedule_time='10:29', delete_report_id=report.id)

    ScheduleManager(prepared_request).delete_schedule()

    assert Report.objects.all().count() == 0


@pytest.mark.django_db
def test_get_reports(report_factory, user_factory, request_factory):
    user = user_factory(username='test_user', password='test', email='test')
    for time in (1, 2, 3):
        report_factory(time=f'10:2{time}', owner=user)
    prepared_request = request_factory(user)

    reports = ScheduleManager(prepared_request).get_reports()

    assert len(reports) == 3
