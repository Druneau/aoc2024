def parse_lines(filepath, delimiter=None, transform=lambda x: x):

    result = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if delimiter is None:
                result.append(transform(line))
            elif delimiter in line:
                result.append(transform(line.split(delimiter)))
    return result


def read_file_as_tuples(filepath):
    def transform(parts):
        parts = parts.split()
        if len(parts) == 2:
            return int(parts[0]), int(parts[1])
        raise ValueError(f"Invalid line format: {' '.join(parts)}")

    return parse_lines(filepath, transform=transform)


def read_file_as_lists(filepath):
    return parse_lines(
        filepath, delimiter=" ", transform=lambda parts: [int(val) for val in parts]
    )


def read_file_as_strings(filepath):
    return parse_lines(filepath)


def read_file_as_chars(filepath):
    return parse_lines(
        filepath, delimiter=None, transform=lambda line: list(line.rstrip())
    )


def read_file_as_string(filepath):
    with open(filepath, "r") as file:
        return file.read()


def read_file_as_dict(file_path, ignore_char=""):
    result = {}
    with open(file_path, "r") as file:
        for y, line in enumerate(file):
            line = line.strip()
            for x, char in enumerate(line):
                if not char == ignore_char:
                    result.setdefault(char, []).append((x, y))
    print(result)
    return result
