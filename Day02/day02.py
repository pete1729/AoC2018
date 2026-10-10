import itertools
import sys


def parse(filename):
    changes = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            changes.append(int(line))
    return changes


def part1(changes):
    return sum(changes)


def part2(changes):
    curr_freq = 0
    frequencies = {0}
    for change in itertools.cycle(changes):
        curr_freq += change
        if curr_freq in frequencies:
            return curr_freq
        frequencies.add(curr_freq)


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    changes = parse(filename)

    assert part1([+1, -2, +3, +1]) == 3
    assert part1([+1, +1, +1]) == 3
    assert part1([+1, +1, -2]) == 0
    assert part1([-1, -2, -3]) == -6

    assert part2([+1, -2, +3, +1]) == 2
    assert part2([+1, -1]) == 0
    assert part2([+3, +3, +4, -2, -4]) == 10
    assert part2([-6, +3, +8, +5, -6]) == 5
    assert part2([+7, +7, -2, -7, -4]) == 14

    print("Resulting Frequency:", part1(changes))
    print("First frequency reached twice:", part2(changes))