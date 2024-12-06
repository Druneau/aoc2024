from collections import defaultdict, deque
from tools.file import parse_lines


def parse_rules(filepath):
    return parse_lines(filepath, "|", lambda parts: tuple(map(int, parts)))


def parse_updates(filepath):
    return parse_lines(filepath, ",", lambda parts: list(map(int, parts)))


def matching_rules(rules, pages):
    set_pages = set(pages)
    return [rule for rule in rules if rule[0] in set_pages and rule[1] in set_pages]


def determine_print_order(rules):

    incoming_pages_count = defaultdict(int)

    for rule_left, rule_right in rules:
        incoming_pages_count[rule_right] += 1
        incoming_pages_count.setdefault(rule_left, 0)

    return sorted(incoming_pages_count, key=lambda k: incoming_pages_count[k])


def process_updates(filepath, condition_fn):
    rules = parse_rules(filepath)
    updates = parse_updates(filepath)

    total_sum = 0
    for update in updates:
        matches = matching_rules(rules, update)
        order = determine_print_order(matches)

        if condition_fn(order, update):
            total_sum += order[len(order) // 2]

    return total_sum


def part1(filepath):
    return process_updates(filepath, lambda order, update: order == update)


def part2(filepath):
    return process_updates(filepath, lambda order, update: order != update)
