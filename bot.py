from utils.action_decorator import ActionDecorator
import handlers

class Bot:
    def __init__(self):
        self.handlers = ActionDecorator.handlers

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