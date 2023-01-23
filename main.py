# local modules
import questions
import states

# other modules
import random


quiz = states.QuizState(1)


def main():
    quiz.ask()


if __name__ == '__main__':
    main()
