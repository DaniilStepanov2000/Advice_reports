import json

from django.contrib.auth.models import User
from django.http import HttpRequest

from .exceptions import IncorrectCredentialsError, UserExists
from django.db.models import Q
from .forms import SignUpForm
import logging
from .views import page404

logger = logging.getLogger('django')


class CredentialsMiddleware:
    errors = None

    def __init__(self, get_response):
        self.get_response = get_response

    def check_form(self, request: HttpRequest) -> None:
        form = SignUpForm(request.POST)
        if not form.is_valid():
            list_errors = [
                er.get('message') for error in json.loads(form.errors.as_json()).values() for er in error
            ]
            raise IncorrectCredentialsError(f"{' '.join(list_errors)}")

    def check_exist_user(self, request: HttpRequest) -> None:
        if User.objects.filter(
                Q(username=request.POST['login']) | Q(email=request.POST['email'])
        ).exists():
            raise UserExists('Sorry the entered email or login already exist. Try again.')

    def __call__(self, request):
        if request.path_info == '/sign_up/' and request.method == 'POST':
            try:
                self.check_exist_user(request)
                self.check_form(request)
            except (UserExists, IncorrectCredentialsError) as exc:
                return page404(request, exc)

        response = self.get_response(request)

        return response
