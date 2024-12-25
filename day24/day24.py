from tools.file import read_file_as_strings


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


def part1(filepath):
    wires = parse_input(filepath)

    bits_dict = {
        int(key[1:]): solve(wires, key) for key in wires if key.startswith("z")
    }

    binary_str = "".join(
        "1" if bit else "0" for _, bit in sorted(bits_dict.items(), reverse=True)
    )
    return int(binary_str, 2)
