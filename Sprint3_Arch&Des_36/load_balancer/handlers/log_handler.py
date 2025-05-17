from handlers.base_handler import RequestHandler

class LogHandler(RequestHandler):
    def process(self, request):
        print(f"Registrando solicitud: {request.content}")
