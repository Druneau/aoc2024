from tools.file import read_file_as_strings
import copy


def _and(wire1, wire2):
    return wire1 and wire2


def _or(wire1, wire2):
    return wire1 or wire2


def _xor(wire1, wire2):
    return wire1 ^ wire2


def parse_equation(line):
    terms = line.split(" ")

    if len(terms) == 2:
        key = terms[0][:-1]
        value = bool(int(terms[1]))

        return key, value

    if len(terms) == 5:
        term1, operation, term2, _, key = terms

        operations = {"AND": _and, "OR": _or, "XOR": _xor}
        equation = [term1, operations[operation], term2]

        return key, equation


def parse_input(filepath):
    lines = read_file_as_strings(filepath)
    lines = [line for line in lines if line.strip()]

    wires = {key: value for line in lines for key, value in [parse_equation(line)]}
    return wires


def solve(wires, key):
    if isinstance(wires[key], bool):
        return wires[key]

    operand1, func, operand2 = wires[key]

    value1 = solve(wires, operand1)
    value2 = solve(wires, operand2)

    result = func(value1, value2)
    wires[key] = result
    return result


def get_output_bits(solved_wires):
    return [bit for _, bit in sorted(solved_wires.items(), reverse=True)]


def part1(filepath):
    wires = parse_input(filepath)

    bits_dict = {
        int(key[1:]): solve(wires, key) for key in wires if key.startswith("z")
    }

    output_bits = get_output_bits(bits_dict)

    return bits_to_number(output_bits)


def number_to_bits(number, num_bits=None):
    binary_str = bin(number)[2:]
    if num_bits:
        binary_str = binary_str.zfill(num_bits)

    return [bit == "1" for bit in binary_str]


def bits_to_string(bits):
    return "".join("1" if bit else "0" for bit in bits)


def bits_to_number(bits):
    return int(bits_to_string(bits), 2)


def get_bit_count(wires):
    # x34 = 34 bits; find max number
    input_bit_count = max(int(key[1:]) for key in wires if key.startswith("x"))
    output_bit_count = max(int(key[1:]) for key in wires if key.startswith("z"))
    return input_bit_count, output_bit_count


def bits_max_number(bit_count):
    return 2 ^ bit_count - 1


def format_with_prefix(prefix, number, width):
    return f"{prefix}{number:0{width}d}"


def update_input_bits(wires, x_bits, y_bits):
    for number, bit in enumerate(x_bits):
        wires[format_with_prefix("x", number, 2)] = bit

    for number, bit in enumerate(y_bits):
        wires[format_with_prefix("y", number, 2)] = bit


def part2(filepath):
    wires = parse_input(filepath)

    input_bit_count, output_bit_count = get_bit_count(wires)

    input_max_number = bits_max_number(input_bit_count)
    output_max_number = bits_max_number(output_bit_count)

    print(f"{input_bit_count}bit inputs --> {input_max_number}")
    print(f"{output_bit_count}bit output --> {output_max_number}")

    for x_number in range(input_max_number):
        x_bits = number_to_bits(x_number)
        for y_number in range(input_max_number):
            simulation_wires = copy.deepcopy(wires)

            y_bits = number_to_bits(y_number)

            update_input_bits(simulation_wires, x_bits, y_bits)

            output_bits = {
                int(key[1:]): solve(simulation_wires, key)
                for key in wires
                if key.startswith("z")
            }

            output_bits_list = get_output_bits(output_bits)

            real_z_bits = number_to_bits(x_number + y_number, output_bit_count + 1)
            print(f"{x_number} + {y_number} = {x_number+y_number}")
            print(bits_to_string(output_bits_list))
            print(bits_to_string(real_z_bits))
