from django.shortcuts import redirect
from django.conf import settings
import logging

logger = logging.getLogger('django')


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path_info not in settings.AUTH_EXC_URLS:
            return redirect('/login/')

        response = self.get_response(request)

        return response
