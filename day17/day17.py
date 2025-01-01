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

    registers = {}
    for line in lines:
        if "Register" in line:
            key, value = line.split(":")
            registers[key.strip().split()[1]] = int(value.strip())

    program_line = [line for line in lines if "Program" in line][0]
    program = list(map(int, program_line.split(":")[1].strip().split(",")))

    return registers, program


def part1(filepath):
    registers, program = parse_program(filepath)

    computer = Computer()
    computer.load_program(registers, program)
    computer.run()

    return computer.output


def part2(filepath):
    registers, program = parse_program(filepath)

    bits = len(program)
    bit_multipliers = [0] * bits
    current_bit_index = bits - 1

    register_a = calculate_register_a_from_bits(bit_multipliers)
    print(register_a)

    while True:
        computer = Computer()
        registers["A"] = register_a
        computer.load_program(registers, program)
        computer.run()

        output = [int(num) for num in computer.output.split(",")]
        if program == output:
            break

        if program[current_bit_index:] == output[current_bit_index:]:
            current_bit_index -= 1
        else:
            bit_multipliers[current_bit_index] += 1

            while bit_multipliers[current_bit_index] == 8:
                bit_multipliers[current_bit_index] = 0
                current_bit_index += 1
                bit_multipliers[current_bit_index] += 1

        register_a = calculate_register_a_from_bits(bit_multipliers)

    print(f"In :{program}")
    print(f"Out:{output}")
    print(f"reg_a:{register_a}")
    print(f"bit_multipliers:{bit_multipliers}")
    return register_a


def calculate_register_a_from_bits(bit_multipliers):
    register_a = 0
    for index, multiplier in enumerate(bit_multipliers):
        register_a += multiplier * 2 ** (3 * index)

    return register_a
