class Server:
    def __init__(self, name):
        self.name = name

    def handle_request(self, request):
        print(f"Servidor {self.name} está manejando la solicitud: {request.content}")
