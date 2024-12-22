from tools.file import read_file_as_ints


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
