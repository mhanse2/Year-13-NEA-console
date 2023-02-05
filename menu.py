class Option:
    def __init__(self, description, command):
        self.description = description
        self.command = command

    def run_command(self):
        eval(self.command)


class Menu:
    def __init__(self, initial=None):
        self.options = []
        if initial is not None:
            for i in initial:
                self.add_option(i)

    def add_option(self, option):
        self.options.append(option)

    def display(self):
        print('What would you like to do?')
        for position, option in enumerate(self.options, 1):
            print(f'{position} - {option.description}')
