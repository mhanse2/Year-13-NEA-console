# local modules
from states import *

quiz = QuizState()

user = UserState()

menu = MenuState([
    ['Start Quiz', 'init_quiz()'],
    ['Display account info', 'user.print_info()'],
    ['Create a new account', 'user.sign_up()'],
    ['Log into an existing account', 'user.log_in()'],
    ['Log out', 'user.log_out()']
])


def main():
    while True:
        if user.cur_user is None:
            print('Welcome! You\'re currently a guest.')
        else:
            print(f'Welcome, {user.cur_user.name}!')
        menu.display()
        choice = menu.prompt()
        eval(choice[1])


def init_quiz():
    if user.cur_user is None:
        quiz.start(1)
    else:
        quiz.start(user.cur_user.level)

    # runs after the quiz is exited
    user.update_level(quiz.final_level)


if __name__ == '__main__':
    main()
