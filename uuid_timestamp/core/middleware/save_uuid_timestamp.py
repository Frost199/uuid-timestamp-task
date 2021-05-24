from timestamp.models import UniqueIdentifierTimestamp


class SaveUuidTimestampMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

    @staticmethod
    def process_response(_, response):
        """Let's handle old-style response processing here, as usual."""
        # Do something with response, possibly using request.
        return response

    @staticmethod
    def process_request(request):
        UniqueIdentifierTimestamp.objects.create()
        return None
