import re

def get_input(filename):
    with open(filename) as f:
        raw_data = f.read()
    reg_a = int(re.search('Register A: (\d+)', raw_data).group(1))
    reg_b = int(re.search('Register B: (\d+)', raw_data).group(1))
    reg_c = int(re.search('Register C: (\d+)', raw_data).group(1))
    program = list(map(int,re.search(r'Program: ((\d,?)+)',raw_data).group(1).split(',')))
    return reg_a, reg_b, reg_c, program


class ChronoComputer:
    def __init__(self, reg_a, reg_b, reg_c, program):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.program = program
        self.pointer = 0
        self.output = []


    def adv(self, operand):
        denominator = 2 ** self.combo(operand)
        self.reg_a = self.reg_a // denominator
        self.pointer += 2


    def bxl(self, operand):
        self.reg_b = self.reg_b ^ operand
        self.pointer += 2

    def bst(self, operand):
        self.reg_b = self.combo(operand) % 8
        self.pointer += 2


    def jnz(self, operand):
        if self.reg_a == 0:
            self.pointer += 2
        else:
            self.pointer = operand


    def bxc(self, operand):
        self.reg_b = self.reg_b ^ self.reg_c
        self.pointer += 2


    def out(self, operand):
        self.output.append(self.combo(operand) % 8)
        self.pointer += 2


    def bdv(self, operand):

        denominator = 2 ** self.combo(operand)
        self.reg_b = self.reg_b // denominator
        self.pointer += 2


    def cdv(self, operand):
        denominator = 2 ** self.combo(operand)
        self.reg_c = self.reg_c // denominator
        self.pointer += 2


    def combo(self, operand):
        if 4 > operand >= 0:
            return operand
        elif operand == 4:
            return self.reg_a
        elif operand == 5:
            return self.reg_b
        elif operand == 6:
            return self.reg_c
        elif operand == 7:
            raise Exception

    def choose_func(self, instruction):
        match instruction:
            case 0:
                return self.adv
            case 1:
                return self.bxl
            case 2:
                return self.bst
            case 3:
                return self.jnz
            case 4:
                return self.bxc
            case 5:
                return self.out
            case 6:
                return self.bdv
            case 7:
                return self.cdv


    def execute(self):
        while self.pointer < len(self.program) - 1:
            func = self.choose_func(self.program[self.pointer])
            operand = self.program[self.pointer + 1]
            func(operand)


def main():
    reg_a, reg_b, reg_c, program = get_input('input_data')
    computer = ChronoComputer(reg_a, reg_b, reg_c, program)
    computer.execute()
    print(','.join(map(str, computer.output)))


if __name__ == '__main__':
    main()

