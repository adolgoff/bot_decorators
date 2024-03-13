from utils.action_handler import AbstractActionHandler
from utils.action_decorator import ActionDecorator

@ActionDecorator("/help")
class HelpHandler(AbstractActionHandler):
    def handle(self, message):
        print("Доступные команды:")
        print("/hello - приветствие")
        print("/bye - прощание")
        print("/help - список доступных команд")