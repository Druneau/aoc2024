def print_array(array):
    for line in array:
        print("".join(line))


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
