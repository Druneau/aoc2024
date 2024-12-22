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
        prices = generate_prices(seed, rounds)

        sequences = extract_sequences(prices)
        banana_price_index = find_first_occurrence_sequences(sequences, prices)

        merge_banana_sequence_price(all_banana_dict, banana_price_index)

    max_key, max_sum = find_max_bananas(all_banana_dict)
    print(f"{max_key}, {max_sum}")

    return max_sum


def generate_prices(seed, rounds):
    day_number = seed
    prices = []
    for _ in range(rounds):
        day_number = evolve_secret(day_number)
        prices.append(price(day_number))
    return prices


def extract_sequences(prices):
    changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    return list(zip(changes, changes[1:], changes[2:], changes[3:]))


def find_first_occurrence_sequences(sequences, prices):
    banana_price_index = {}
    for i, seq in enumerate(sequences):
        current_price = prices[i + 4]  # Offset to align with the sequence
        if seq not in banana_price_index:  # Only store the first occurrence
            banana_price_index[seq] = current_price
    return banana_price_index


def merge_banana_sequence_price(all_banana_dict, banana_price_index):
    for seq, value in banana_price_index.items():
        if seq not in all_banana_dict:
            all_banana_dict[seq] = []
        all_banana_dict[seq].append(value)


def find_max_bananas(all_banana_dict):
    max_key = max(all_banana_dict, key=lambda k: sum(all_banana_dict[k]))
    max_sum = sum(all_banana_dict[max_key])
    return max_key, max_sum
