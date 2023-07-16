import pytest
from django.contrib.auth.models import User
from django.http import HttpRequest

from main_api.models import Report


@pytest.fixture
def report_factory():
    def factory(time, owner):
        report = Report.objects.create(
            title='',
            time=time,
            owner=owner
        )
        return report
    return factory


@pytest.fixture
def user_factory():
    def factory(username, password, email):
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        return user
    return factory


@pytest.fixture
def request_factory():
    def factory(user, **kwargs):
        prepared_request = HttpRequest()
        prepared_request.POST = kwargs
        prepared_request.user = user
        return prepared_request
    return factory
