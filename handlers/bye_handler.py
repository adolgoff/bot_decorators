from utils.action_handler import AbstractActionHandler
from utils.action_decorator import ActionDecorator

@ActionDecorator("/bye")
class ByeHandler(AbstractActionHandler):
    def handle(self, message):
        print("Пока! Увидимся позже.")