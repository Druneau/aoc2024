def read_file_as_tuples(filename):
    result = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    result.append((int(parts[0]), int(parts[1])))
                else:
                    raise ValueError(f"Invalid line format: {line.strip()}")
    except Exception as e:
        print(f"An error occured: {e}")
    return result


def read_file_as_lists(filename):
    result = []
    try:
        with open(filename, "r") as file:
            for line in file:
                result.append([int(val) for val in line.split()])
    except Exception as e:
        print(f"An error occured: {e}")
    return result


def read_file_as_strings(filename):
    result = []
    try:
        with open(filename, "r") as file:
            for line in file:
                result.append(line.rstrip())
    except Exception as e:
        print(f"An error occured: {e}")
    return result


def read_file_as_chars(filename):
    result = []
    try:
        with open(filename, "r") as file:
            for line in file:
                result.append(list(line.rstrip()))
    except Exception as e:
        print(f"An error occure: {e}")
    return result
