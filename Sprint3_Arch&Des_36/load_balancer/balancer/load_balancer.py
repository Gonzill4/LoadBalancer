# Observer (RequestLogger observa a LoadBalancer)

from core.server_factory import ServerFactory

class LoadBalancer:
    def __init__(self):
        self.observers = []
        self.current_index = 0
        self.handler_chain = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def set_handler_chain(self, handler):
        self.handler_chain = handler

    def dispatch_request(self, request):
        servers = ServerFactory.get_instance().get_servers()
        if not servers:
            print("No hay servidores disponibles.")
            return

        # Round Robin
        server = servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(servers)

        # Chain of Responsibility
        if self.handler_chain:
            self.handler_chain.handle(request)

        # Notificar observadores
        for observer in self.observers:
            observer.on_request_dispatched(server, request)

        # Enviar solicitud al servidor
        server.handle_request(request)
