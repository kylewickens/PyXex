class Indents:
    def __init__(self):
        self.amount = ''

    def indent(self):
        self.amount += ' '

    def outdent(self):
        self.amount = self.amount[1:]

    def output(self, name, *args):
        output = self.amount + name
        if args:
            output += ' ='
        for arg in args:
            output += ' ' + str(arg)
        print(output)
