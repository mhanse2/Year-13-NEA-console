# local modules
import levels
import questions
from user import User
from util import FERNET, CUTOFF

# other modules
import random
import sqlite3


# MENU STATE #
class MenuState:
    def __init__(self, initial=None):
        self.options = []
        if initial is not None:
            for i in initial:
                self.add_option(i)

    def add_option(self, option):
        self.options.append(option)

    def display(self):
        print('What would you like to do?')
        for position, option in enumerate(self.options):
            print(f'{position + 1} - {option[0]}')

    def prompt(self):
        try:
            ans = int(input('> '))
            return self.options[ans - 1]

        except ValueError:
            print('Your answer is not a number. Please try again.')
            self.prompt()

        except IndexError:
            print('Your answer is out of range. Please try again.')
            self.prompt()


# QUIZ STATE #
class QuizState:
    def __init__(self):
        self.queue = []
        self.finished = []
        self.current = None
        self.lives = 3
        self.exiting = False
        self.final_level = 1

    def start(self, level):
        print('Quiz is starting. Please type "EXIT" to exit the quiz and save your progress.')
        for i in range(3):
            self._generate_question(level)
        self.current = self.queue[0]
        self.lives = 3
        self.final_level = level
        self.ask()

    def next_question(self, correct):
        q = self.queue.pop(0)
        if len(self.finished) == 10:
            self.finished.pop(0)
        self.finished.append(q)
        while len(self.queue) < 3:
            self._generate_question(q.level, correct)
        self.current = self.queue[0]
        self.lives = 3

    def ask(self):
        print(f'Lives left: {self.lives}')
        print(f'\n{self.current}')
        try:
            raw_ans = input('= ')
            answer = float(raw_ans)
            if answer == self.current.ans:
                print('Correct!')
                self.next_question(True)
            else:
                print('Incorrect.')
                self.lives -= 1 if self.lives > 1 else self.next_question(False)

        except ValueError:
            if raw_ans == 'EXIT' or 'Exit' or 'exit':
                self.exiting = True
            else:
                print('Your answer is not an number.')

        finally:
            if not self.exiting:
                self.ask()
            else:
                self.exit()

    def exit(self):
        self.final_level = self.current.level

    def _generate_question(self, old, correct=None):
        new = old
        if (correct is not None) and (old < 12):
            if correct:
                new += 1
            else:
                new -= 1
        self.queue.append(eval(
            f'questions.{levels.order[random.randint(0, new - 1)]}({new})'
        ))


# USER STATE #
class UserState:
    def __init__(self):
        self.cur_user = None
        self.db_connection = sqlite3.connect('userdata.db')
        self.db = self.db_connection.cursor()
        # self.db.execute('''
        #     CREATE TABLE users(
        #                       id INTEGER NOT NULL PRIMARY KEY,
        #                       name TEXT NOT NULL,
        #                       pass TEXT NOT NULL,
        #                       level INTEGER NOT NULL);
        # ''')

    def sign_up(self):
        user_inputted = False
        pass_inputted = False
        username = ''
        password = ''

        while not user_inputted:
            username = input('Please enter your username.\n> ')
            if len(username) > 2:
                user_inputted = True
            elif len(username) < 3:
                print('Use more than two characters.')

        while not pass_inputted:
            password = input('Please enter your password.\n> ')
            if len(password) > 2:
                pass_inputted = True
            elif len(password) < 3:
                print('Use more than two characters.')

        self.db.execute(f'''
            INSERT INTO users (name, pass, level)
            VALUES ('{username}', '{password}', 1);
        ''')
        self.db_connection.commit()

        print('New user created. Please log in to use your account.')

    def log_in(self):
        try:
            username = input('Username: ')
            password = input('Password: ')
            self.db.execute(f'''
                SELECT name, pass, level
                FROM users
                WHERE name = '{username}'
                AND pass = '{password}';
            ''')
            selection = self.db.fetchall()
            print(selection)
            self.cur_user = User(selection[0][0], selection[0][1], selection[0][2])

        except sqlite3.OperationalError:
            print('[ERROR] User does not exist. Please check your inputs and try again.')

    def log_out(self):
        print('You\'ve been logged out.')
        self.cur_user = None

    def print_info(self):
        if self.cur_user is None:
            print('You are currently a guest. Please create an account or log in to save your progress.')
        else:
            print(f'''
            {self.cur_user.name}
            Level: {self.cur_user.level}
            ''')

    def update_level(self, new_level):
        if self.cur_user is None:
            pass
        else:
            self.db.execute(f'''
                            UPDATE users
                            SET level = {new_level}
                            WHERE name = '{self.cur_user.name}';
                        ''')
            self.db_connection.commit()
            self.cur_user.level = new_level
