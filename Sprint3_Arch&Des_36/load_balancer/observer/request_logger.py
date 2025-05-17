from observer.observer import Observer

class RequestLogger(Observer):
    def on_request_dispatched(self, server, request):
        print(f"LOG: Solicitud enviada a {server.name}: {request.content}")
