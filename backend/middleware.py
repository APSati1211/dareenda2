# backend/middleware.py
from django.utils.deprecation import MiddlewareMixin

class ConditionalCoopMiddleware(MiddlewareMixin):
    """
    Add Cross-Origin-Opener-Policy only for secure or localhost origins.
    Prevents browsers from ignoring the header on non-trustworthy origins.
    """
    def process_response(self, request, response):
        host = request.get_host().split(':')[0]
        if request.is_secure() or host in ('localhost', '127.0.0.1'):
            response['Cross-Origin-Opener-Policy'] = 'same-origin'
        return response

