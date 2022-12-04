file = open("2022_3_AOC_input.txt").read()
parts = file.split("\n")

# part one
sum_priorities = 0
for line in parts:
    first_part, second_part = line.strip()[:len(line) // 2], line.strip()[len(line) // 2:]
    e = (set(first_part) & set(second_part)).pop()
    if e >= "a":
        sum_priorities += ord(e) - ord("a") + 1
    else:
        sum_priorities += ord(e) - ord("A") + 26 + 1

print(sum_priorities)
sum_priorities = 0

# part two

index = 0
while index < len(parts):
    elf_one, elf_two, elf_three = parts[index: index + 3]
    index += 3
    e = (set(elf_one) & set(elf_two) & set(elf_three)).pop()
    if e >= "a":
        sum_priorities += ord(e) - ord("a") + 1
    else:
        sum_priorities += ord(e) - ord("A") + 26 + 1

print(sum_priorities)
