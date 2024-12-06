from collections import defaultdict, deque
from tools.file import parse_lines


def parse_rules(filepath):
    return parse_lines(filepath, "|", lambda parts: tuple(map(int, parts)))


def parse_updates(filepath):
    return parse_lines(filepath, ",", lambda parts: list(map(int, parts)))


def matching_rules(rules, pages):
    set_pages = set(pages)
    return [rule for rule in rules if rule[0] in set_pages and rule[1] in set_pages]


def find_page_order(edges):

    pages_after = defaultdict(list)
    count_pages_before = defaultdict(int)

    for page_before, next_page in edges:
        pages_after[page_before].append(next_page)
        count_pages_before[next_page] += 1
        count_pages_before.setdefault(page_before, 0)

    # topological sort
    ready_pages = deque(
        [node for node in count_pages_before if count_pages_before[node] == 0]
    )
    page_order = []
    while ready_pages:
        current_page = ready_pages.popleft()
        page_order.append(current_page)

        for next_page in pages_after[current_page]:
            count_pages_before[next_page] -= 1

            if count_pages_before[next_page] == 0:
                ready_pages.append(next_page)

    return page_order


def process_updates(filepath, condition_fn):
    rules = parse_rules(filepath)
    updates = parse_updates(filepath)

    total_sum = 0
    for update in updates:
        matches = matching_rules(rules, update)
        order = find_page_order(matches)

        if condition_fn(order, update):
            total_sum += order[len(order) // 2]

    return total_sum


def part1(filepath):
    return process_updates(filepath, lambda order, update: order == update)


def part2(filepath):
    return process_updates(filepath, lambda order, update: order != update)
