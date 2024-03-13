from utils.action_handler import AbstractActionHandler
from utils.action_decorator import ActionDecorator

@ActionDecorator("/hello")
class HelloHandler(AbstractActionHandler):
    def handle(self, message):
        print("Привет! Как дела?")