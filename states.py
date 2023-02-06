import random
import questions
import levels


# MENU STATE #
class Option:
    def __init__(self, description, command):
        self.description = description
        self.command = command


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
            print(f'{position + 1} - {option.description}')

    def prompt(self):
        try:
            ans = int(input('> '))
            return self.options[ans - 1]

        except ValueError:
            print('Your answer is not a number. Please try again.')
            self.prompt()


# QUIZ STATE #
class QuizState:
    def __init__(self, level):
        self.queue = []
        for i in range(3):
            self._generate_question(level)
        self.finished = []
        self.current = self.queue[0]
        self.lives = 3

    def override_level(self, new_level):
        if new_level < 13:
            self.level = new_level
        else:
            print('[ERROR] Level out of range.')

    def next_question(self, correct):
        q = self.queue.pop(0)
        if len(self.finished) == 10:
            self.finished.pop(0)
        self.finished.append(q)
        self._generate_question(q.level, correct)
        self.current = self.queue[0]
        self.lives = 3

    def ask(self):
        print(self.queue)
        print(self.finished)
        print(f'\n{self.current}')
        try:
            answer = float(input('= '))
            if answer == self.current.ans:
                print('Correct!')
                self.next_question(True)
            else:
                print('Incorrect.')
                self.lives -= 1 if self.lives > 1 else self.next_question(False)

        except ValueError:
            print('Your answer is not an number.')

        finally:
            self.ask()

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
