from tools.file import read_file_as_strings
import sys


class Computer:
    def __init__(self):
        self.registers = {"A": 0, "B": 0, "C": 0}
        self.instruction_pointer = 0
        self.program = []
        self.instructions = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        self.output = None

    def load_program(self, registers, program):
        self.registers = registers
        self.program = program
        self.instruction_pointer = 0

    def reset(self):
        self.program = []
        self.instruction_pointer = 0
        self.registers["A"] = 0
        self.registers["B"] = 0
        self.registers["C"] = 0

    def run(self):
        while self.instruction_pointer < len(self.program):
            opcode, *operands = (
                self.program[self.instruction_pointer],
                self.program[self.instruction_pointer + 1],
            )
            if opcode in self.instructions:
                self.instructions[opcode](*operands)
            else:
                print(f"Invalid opcode: {opcode}")
                break
            self.instruction_pointer += 2

    def combo(self, operand):
        if operand == 4:
            return self.registers["A"]
        if operand == 5:
            return self.registers["B"]
        if operand == 6:
            return self.registers["C"]
        if operand == 7:
            raise ValueError(f"Invalid combo operand: {operand}")

        return operand

    def adv(self, operand):
        numerator = self.registers["A"]
        denominator = 2 ** self.combo(operand)
        self.registers["A"] = numerator // denominator

    def bxl(self, operand):
        self.registers["B"] = self.registers["B"] ^ operand

    def bst(self, operand):
        combo_operand = self.combo(operand)
        self.registers["B"] = combo_operand % 8

    def jnz(self, operand):
        if self.registers["A"] == 0:
            return

        self.instruction_pointer = operand - 2

    def bxc(self, operand):
        self.registers["B"] = self.registers["B"] ^ self.registers["C"]

    def out(self, operand):
        result = self.combo(operand) % 8
        if self.output:
            self.output = self.output + "," + str(result)
        else:
            self.output = str(result)

    def bdv(self, operand):
        numerator = self.registers["A"]
        denominator = 2 ** self.combo(operand)
        self.registers["B"] = numerator // denominator

    def cdv(self, operand):
        numerator = self.registers["A"]
        denominator = 2 ** self.combo(operand)
        self.registers["C"] = numerator // denominator


def parse_program(filepath):
    lines = read_file_as_strings(filepath)

    # Extract register values
    registers = {}
    for line in lines:
        if "Register" in line:
            key, value = line.split(":")
            registers[key.strip().split()[1]] = int(value.strip())

    # Extract program
    program_line = [line for line in lines if "Program" in line][0]
    program = list(map(int, program_line.split(":")[1].strip().split(",")))

    return registers, program


def part1(filepath):
    registers, program = parse_program(filepath)

    computer = Computer()
    computer.load_program(registers, program)
    computer.run()

    return computer.output


def part2(filepath, register_a_start_value=0):
    registers, program = parse_program(filepath)

    register_a = register_a_start_value

    while True:
        computer = Computer()
        registers["A"] = register_a
        computer.load_program(registers, program)
        computer.run()

        output = [int(num) for num in computer.output.split(",")]
        print(f"register_a:{register_a}")
        print_as_bits(program)
        print_as_bits(output)
        if program == output:
            print(f"register_a:{register_a}")
            print_as_bits(program)
            print_as_bits(output)
            break

        break
        register_a += 1

    return register_a


def geometric_series(terms):
    return [2 ** (3 * n) for n in range(terms)]


def get_as_bits(list):
    return f"{[format(num, "03b") for num in list]} --> {list}"


def print_as_bits(list):
    for num in list:
        print(f"{format(num, '03b')}", end=" ")
    print(f"-->{list}")


if __name__ == "__main__":
    print(geometric_series(16))
    register_a = part2("day17/input.txt", int(sys.argv[1]))
