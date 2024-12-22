from tools.file import read_file_as_ints
from tools.debug import write_and_open_in_nvim


def mix(secret, number):
    return secret ^ number


def prune(secret):
    return secret % 16777216


def mix_and_prune(secret, number):
    return prune(mix(secret, number))


def evolve_secret(secret):
    step1 = mix_and_prune(secret, secret * 64)
    step2 = mix_and_prune(step1, step1 // 32)
    step3 = mix_and_prune(step2, step2 * 2048)

    return step3


def part1(filepath, rounds):
    seeds = read_file_as_ints(filepath)

    # we're gonna need to cache results...
    total_sum = 0
    for seed in seeds:
        day_number = seed
        for _ in range(rounds):
            day_number = evolve_secret(day_number)
        total_sum += day_number

    return total_sum


def price(secret):
    return secret % 10


def part2(filepath, rounds):
    seeds = read_file_as_ints(filepath)

    all_banana_dict = {}

    for seed in seeds:
        day_number = seed

        prices = []

        for _ in range(rounds):
            day_number = evolve_secret(day_number)
            prices.append(price(day_number))

        changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        sequences = list(zip(changes, changes[1:], changes[2:], changes[3:]))

        if len(prices) != rounds or len(sequences) != rounds - 4:
            raise ValueError("should not happen")

        banana_price_index = {}
        for i, seq in enumerate(sequences):
            current_price = prices[i + 4]  # Offset to align with the sequence
            # THIS IS WHAT TRIPPED ME UP FOR 2 HOURS...
            # if more than 1 sequence same... only FIRST one will be hit
            if seq not in banana_price_index:
                banana_price_index[seq] = current_price

        for seq, value in banana_price_index.items():
            if seq not in all_banana_dict:
                all_banana_dict[seq] = []
            all_banana_dict[seq].append(value)

    max_key = max(all_banana_dict, key=lambda k: sum(all_banana_dict[k]))
    max_sum = sum(all_banana_dict[max_key])

    print(f"{max_key}, {max_sum}")

    # write_and_open_in_nvim(all_banana_dict)

    return max_sum
