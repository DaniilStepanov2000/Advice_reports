import pytest
from django.contrib.auth.models import User


def test_auth_login(client):
    result = client.get('/login/')

    assert result.status_code == 200
    assert result.templates[0].name == 'main_api/login.html'


@pytest.mark.django_db
def test_register_new_user(
        client, user_factory
):
    user = user_factory(username='test', password='test', email='test')
    client.login(username=user.username, password='test')
    result = client.get('/')

    assert result.status_code == 200
    assert result.templates[0].name == 'main_api/random_word.html'
    assert User.objects.count() == 1
