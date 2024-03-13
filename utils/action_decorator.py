class ActionDecorator:
    handlers = {}

    def __init__(self, command):
        self.command = command

    def __call__(self, cls):
        cls.command = self.command
        ActionDecorator.handlers[self.command] = cls()
        return cls