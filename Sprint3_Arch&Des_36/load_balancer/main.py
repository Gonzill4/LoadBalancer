# Team 36 - Sprint 3 - Load Balancer

from core.server_factory import ServerFactory
from core.server import Server
from core.request import Request

from balancer.load_balancer import LoadBalancer
from observer.request_logger import RequestLogger

from handlers.auth_handler import AuthHandler
from handlers.log_handler import LogHandler

if __name__ == "__main__":
    #  servidores
    factory = ServerFactory.get_instance()
    factory.add_server(Server("Servidor-1"))
    factory.add_server(Server("Servidor-2"))
    factory.add_server(Server("Servidor-3"))

    #  load balancer
    balancer = LoadBalancer()
    balancer.add_observer(RequestLogger())

    #  responsabilidades
    auth = AuthHandler()
    log = LogHandler()
    auth.set_next(log)
    balancer.set_handler_chain(auth)

    # Enviar solicitudes
    balancer.dispatch_request(Request("Petición A"))
    balancer.dispatch_request(Request("Petición B"))
    balancer.dispatch_request(Request("Petición C"))
    balancer.dispatch_request(Request("Petición D"))
