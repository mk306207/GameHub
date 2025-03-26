from django.contrib.messages import get_messages

class ClearMessagesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        messages = get_messages(request)
        messages._loaded = False
        response = self.get_response(request)
        return response