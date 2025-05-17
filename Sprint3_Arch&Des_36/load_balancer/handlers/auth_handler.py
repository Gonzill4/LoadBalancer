from handlers.base_handler import RequestHandler

class AuthHandler(RequestHandler):
    def process(self, request):
        print(f"Autenticando solicitud: {request.content}")
