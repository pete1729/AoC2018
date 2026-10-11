import re
import sys

import numpy as np

FABRIC_SIZE = 1000


def parse(filename):
    with open(filename, encoding="utf-8") as file:
        claims = [[int(n) for n in re.findall(r"\d+", line)] for line in file]
    return claims


def build_fabric(claims):
    fabric = np.zeros((FABRIC_SIZE, FABRIC_SIZE), dtype=int)
    for line_split in claims:
        claim_id, start_x, start_y, x_size, y_size = line_split
        fabric[start_x:start_x + x_size, start_y:start_y + y_size] += 1
    return fabric


def part1(claims):
    fabric = build_fabric(claims)
    return (fabric > 1).sum()


def part2(claims):
    fabric = build_fabric(claims)
    for line_split in claims:
        claim_id, start_x, start_y, x_size, y_size = line_split
        area = fabric[start_x:start_x + x_size, start_y:start_y + y_size]
        if (area == 1).all():
            return claim_id


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    test_claims = parse("test_input.txt")
    assert part1(test_claims) == 4
    assert part2(test_claims) == 3

    claims = parse(filename)
    print("Sum of multiples:", part1(claims))
    print("Fabric not reused:", part2(claims))
