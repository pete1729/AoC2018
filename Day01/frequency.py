filename = "input.txt"

curr_freq = 0

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        curr_freq += int(line.strip())

print("Resulting Frequency:", curr_freq)