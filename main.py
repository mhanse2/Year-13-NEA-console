# local modules
from states import *


quiz = QuizState(1)

menu = MenuState([
    Option('Start Quiz', 'quiz.ask()'),
    Option('Print Hello World', 'print(\'Hello World!\')')
])


def main():
    while True:
        menu.display()
        choice = menu.prompt()
        eval(choice.command)


if __name__ == '__main__':
    main()
