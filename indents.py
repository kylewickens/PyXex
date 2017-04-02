class Indents:
    def __init__(self):
        self.amount = ''

    def _hex2(self, value):
        return '0x' + format(value,  '02x')

    def _hex8(self, value):
        return '0x' + format(value,  '08x')

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

    def output_hex2(self, name, value, *args):
        self.output(name, self._hex2(value), *args)

    def output_hex8(self, name, value, *args):
        self.output(name, self._hex8(value), *args)
