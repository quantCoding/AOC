file = open("2022_4_AOC_input.txt").read()

# part one
section_one = []
section_two = []
for line in file.split("\n"):
    parts = line.split(",")
    section_one.append((int(parts[0].split("-")[0]), int(parts[0].split("-")[1])))
    section_two.append((int(parts[1].split("-")[0]), int(parts[1].split("-")[1])))


index = 0
counter_section = 0
while index < len(section_one):
    first = section_one[index]
    second = section_two[index]
    if first[0] <= second[0] and first[1] >= second[1]:
        #print(first, second)
        counter_section += 1

    elif second[0] <= first[0] and second[1] >= first[1]:
        #print(first, second)
        counter_section += 1

    index += 1

print(counter_section)
counter_section = 0
index = 0

# part two
while index < len(section_one):
    overlapping_numbers = set(x for x in range (section_one[index][0], section_one[index][1] + 1)).intersection(set(x for x in range(section_two[index][0], section_two[index][1] + 1)))
    if len(overlapping_numbers) > 0:
        counter_section += 1

    index += 1

print(counter_section)