import pytest

from main_api.models import Report
from main_api.tasks import generate_tasks


@pytest.mark.django_db
def test_send_email(
        settings, mocker, report_factory, user_factory
):
    # CELERY_TASK_ALWAYS_EAGER to run celery tasks synchronously (for debug) and for delay()
    settings.CELERY_TASK_ALWAYS_EAGER = True

    user = user_factory(username='some_user', password='psw', email='test')
    for time in (1, 2, 3):
        report_factory(time=f'10:3{time}', owner=user)

    # return value is True because in successful case task should not fail and final count is 3 (in this test)
    mocked_check_time = mocker.patch('main_api.tasks.check_time', return_value=True)
    mocked_sendmail = mocker.patch('smtplib.SMTP.sendmail', return_value=True)

    generate_tasks.delay()

    assert Report.objects.all().count() == 3
    assert mocked_check_time.call_count == 3
    assert mocked_sendmail.call_count == 3
