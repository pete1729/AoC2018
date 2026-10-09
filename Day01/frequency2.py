filename = "input.txt"

curr_freq = 0

changes = []
frequencies = {0}
count = 0

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        next_change = int(line.strip())
        changes.append(next_change)

while True:
    curr_freq += changes[count % len(changes)]
    count += 1

    if curr_freq in frequencies:
        print("First frequency reached twice:", curr_freq)
        break
    else:
        frequencies.add(curr_freq)