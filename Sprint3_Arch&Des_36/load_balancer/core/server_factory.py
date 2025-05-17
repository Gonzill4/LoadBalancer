# Singleton para la clase ServerFactory

from core.server import Server

class ServerFactory:
    _instance = None

    def __init__(self):
        if ServerFactory._instance is not None:
            raise Exception("Esta clase es un Singleton.")
        self.servers = []
        ServerFactory._instance = self

    @staticmethod
    def get_instance():
        if ServerFactory._instance is None:
            ServerFactory()
        return ServerFactory._instance

    def add_server(self, server: Server):
        self.servers.append(server)

    def get_servers(self):
        return self.servers
