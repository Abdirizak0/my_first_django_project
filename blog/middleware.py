import time
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from django.contrib.auth.models import User
from .models import UserActionLog

class UserActionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        if hasattr(request, 'user') and request.user.is_authenticated:
            execution_time = time.time() - request.start_time
            UserActionLog.objects.create(
                user=request.user,
                action=request.method,
                path=request.path,
                execution_time=execution_time
            )
        return response