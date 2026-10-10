import itertools
import sys
from collections import Counter


def parse(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.strip() for line in file]
    return lines


def part1(lines):
    two_counts = 0
    three_counts = 0

    for line in lines:
        counts = Counter(line).values()
        two_counts += 2 in counts
        three_counts += 3 in counts

    return two_counts * three_counts


def part2(lines):
    for first, second in itertools.combinations(lines, 2):
        match_differences = sum(a != b for a, b in zip(first, second))
        if match_differences == 1:
            return "".join([a for a, b in zip(first, second) if a == b])


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    lines = parse(filename)

    assert part1(["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]) == 12
    assert part2(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]) == "fgij"

    print("Product of two and three counts:", part1(lines))
    print("Common letters:", part2(lines))