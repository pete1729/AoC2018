import itertools
import sys
from collections import Counter


def parse(filename):
    lines = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            lines.append(line.strip())
    return lines


def part1(lines):
    two_counts = 0
    three_counts = 0
    
    for line in lines:
        binary_two = 0
        binary_three = 0
        char_counts = Counter(line)
        for char_count in char_counts.most_common():
            if char_count[1] == 2:
                binary_two = 1
            if char_count[1] == 3:
                binary_three = 1
        two_counts += binary_two
        three_counts += binary_three

    return two_counts*three_counts


def part2(lines):
    for i,line in enumerate(lines):
        for j in range(i,len(lines)):
            match_differences = sum(a != b for a, b in zip(lines[i], lines[j]))
            if match_differences == 1:
                new_line_chars = [a for a, b in zip(lines[i], lines[j]) if a == b]
                output_string = ""
                for char in new_line_chars:
                    output_string += char
                return output_string


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    lines = parse(filename)

    assert part1(["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]) == 12
    assert part2(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]) == "fgij"

    print("Product of two and three counts:", part1(lines))
    print("Common letters:", part2(lines))