input = open("2022_6_AOC_input.txt").read()

p1 = 0
p2 = 0
for i in range(len(input)):
    s = set(input[i:i + 4])
    if p1 == 0 and len(s) == 4:
        p1 = i + 4

    s = set(input[i:i + 14])
    if p2 == 0 and len(s) == 14:
        p2 = i + 14

# part one
print(p1)

# part two
print(p2)