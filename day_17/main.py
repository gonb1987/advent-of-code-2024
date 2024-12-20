import re
from heapq import heappush, heappop


def get_input(filename):
    with open(filename) as f:
        raw_data = f.read()
    reg_a = int(re.search('Register A: (\d+)', raw_data).group(1))
    reg_b = int(re.search('Register B: (\d+)', raw_data).group(1))
    reg_c = int(re.search('Register C: (\d+)', raw_data).group(1))
    program = list(map(int, re.search(r'Program: ((\d,?)+)', raw_data).group(1).split(',')))
    return reg_a, reg_b, reg_c, program


class ChronoComputer:
    """
    Class that implements the computer logic and execute and reset methods to run the program
    and to return the computer to the initial state.
    """
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
        self.reg_b = self.reg_a // denominator
        self.pointer += 2

    def cdv(self, operand):
        denominator = 2 ** self.combo(operand)
        self.reg_c = self.reg_a // denominator
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

    def reset(self):
        self.pointer = 0
        self.output = []


def match_program(computer):
    """
    Dijkstra's implementation for finding the smallest Register A that outputs the program given
    octet by octet starting from the left of register A. The first octet corresponds to the last
    output of the computer and that part of the output isn't modified when we add more octets.
    .
    :param computer:
    :return: smallest register A that outputs the program given
    """
    avail_paths = [(bin(0), -1)]
    while avail_paths:
        a, index_to_match = heappop(avail_paths)
        a = int(a, 2) << 3
        for i in range(8):
            computer.reset()
            computer.reg_a = i + a
            computer.execute()
            if computer.output[0] == computer.program[index_to_match]:
                if computer.output == computer.program:
                    return a + i
                heappush(avail_paths, (bin(a + i), index_to_match - 1))



def main():
    # Set up the computer
    reg_a, reg_b, reg_c, program = get_input('input_data')
    computer = ChronoComputer(reg_a, reg_b, reg_c, program)
    # Run Part 1
    computer.execute()
    print(','.join(map(str, computer.output)))
    # Run part 2
    print(match_program(computer))


if __name__ == '__main__':
    main()
