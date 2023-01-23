import questions


class QuizState:
    def __init__(self, level):
        self.queue = [questions.Addition([4], [5]), questions.Subtraction([2], [6]), questions.Triangle([4], [4])]
        self.finished = []
        self.current = self.queue[0]
        self.lives = 3

    def next_question(self):
        q = self.queue.pop(0)
        self.finished.append(q)
        self._generate_question(q)
        self.current = self.queue[0]
        self.lives = 3

    def ask(self):
        print(f'\n{self.current}')
        try:
            answer = int(input('= '))
            if answer == self.current.ans:
                print('Correct!')
                self.next_question()
            else:
                print('Incorrect.')
                self.lives -= 1 if self.lives > 1 else self.next_question()

        except ValueError:
            print('Your answer is not an integer.')

        finally:
            self.ask()

    def _generate_question(self, old):
        self.queue.append(questions.Addition([1, 2, 3], [1, 2, 3]))
        # TODO
