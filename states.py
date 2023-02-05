import random

import questions
import levels


class QuizState:
    def __init__(self, level):
        self.queue = []
        for i in range(3):
            self._generate_question(level, None)
        self.finished = []
        self.current = self.queue[0]
        self.lives = 3

    def next_question(self, correct):
        q = self.queue.pop(0)
        self.finished.append(q)
        self._generate_question(q.level, correct)
        self.current = self.queue[0]
        self.lives = 3

    def ask(self):
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

    def _generate_question(self, old, correct):
        new = old
        if correct is not None:
            if old < 12 and correct:
                new += 1
            elif old < 12 and not correct:
                new -= 1
        self.queue.append(eval(
            f'questions.{levels.order[random.randint(0, new - 1)]}({new})'
        ))
        # TODO
