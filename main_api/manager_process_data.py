import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

logger = logging.getLogger('django')


class SignUpManager:
    def __init__(self, request):
        self.request = request

    def create_user(self):
        """
        Create user in database
        """
        User.objects.create_user(
            username=self.request.POST["login"],
            email=self.request.POST["email"],
            password=self.request.POST["password"]
        )
        logger.info(
            f'User with {self.request.POST["login"]}; {self.request.POST["email"]}; '
            f'{self.request.POST["password"]} does not exists. Created new user.'
        )


class LoginManager(SignUpManager):

    def login_user(self):
        """
        Check or set session cookies in client
        """
        user = authenticate(
            username=self.request.POST["login"],
            password=self.request.POST["password"]
        )
        if user is not None:
            logger.info(f'User exists, login: {user.username}')
            login(self.request, user)

            return True

    def logout(self):
        """
        Remove cookie from client
        """
        logout(self.request)
