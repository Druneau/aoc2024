from tools.file import read_file_as_strings
from pprint import pprint


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
        value = [bool(int(terms[1]))]

        return (key, value)
    elif len(terms) == 5:
        term1 = terms[0]
        operation = terms[1]
        term2 = terms[2]
        key = terms[4]

        if operation == "AND":
            operation = _and
        elif operation == "OR":
            operation = _or
        elif operation == "XOR":
            operation = _xor

        value = [term1, operation, term2]
        return (key, value)

    return (None, None)


def parse_input(filepath):
    lines = read_file_as_strings(filepath)

    wires = {}

    for line in lines:
        key, value = parse_equation(line)

        if key is None:
            continue
        wires[key] = value

    return wires


def solve(wires, key):
    # If the key already resolves to a value, return it
    if len(wires[key]) == 1:
        return wires[key][0]  # The value is already resolved (True or False)

    # Otherwise, extract [operand1, function, operand2]
    operand1, func, operand2 = wires[key]

    # Resolve operands recursively
    value1 = solve(wires, operand1) if operand1 in wires else operand1
    value2 = solve(wires, operand2) if operand2 in wires else operand2

    # Apply the function and cache the result
    result = func(value1, value2)
    wires[key] = [result]  # Cache the resolved value to avoid recomputation
    return result


def part1(filepath):
    wires = parse_input(filepath)

    bits_dict = {}
    for key in wires:
        if key.startswith("z"):
            key_number = int(key[1:])
            value = solve(wires, key)
            bits_dict[key_number] = value

    bits_dict = dict(sorted(bits_dict.items()))
    bits = [value for key, value in bits_dict.items()]
    bits.reverse()
    binary_str = "".join("1" if bit else "0" for bit in bits)
    decimal_number = int(binary_str, 2)

    return decimal_number
