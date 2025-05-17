class RequestHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request):
        self.process(request)
        if self.next_handler:
            self.next_handler.handle(request)

    def process(self, request):
        raise NotImplementedError("Debes implementar el método process()")
