from utils.action_decorator import ActionDecorator
import os
import importlib

class Bot:
    def __init__(self):
        self.handlers = ActionDecorator.handlers
        self.load_handlers()

    def load_handlers(self):
        handlers_dir = 'handlers'
        for file in os.listdir(handlers_dir):
            if file.endswith('.py') and not file.startswith('__'):
                module_name = file[:-3]
                importlib.import_module(f'{handlers_dir}.{module_name}')

    def handle_message(self, message):
        command = message.split()[0]
        if command in self.handlers:
            handler = self.handlers[command]
            handler.handle(message)
        else:
            print("Неизвестная команда")

# Создание экземпляра бота
bot = Bot()

# Обработка сообщений
while True:
    message = input("Введите сообщение: ")
    bot.handle_message(message)