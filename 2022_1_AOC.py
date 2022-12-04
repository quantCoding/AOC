# part one
file = open("2022_2_AOC_input.txt")

counter_max_calorie = 0
counter_current_elf = 0
for line in file:
    if line != "\n" and line != "":
        counter_current_elf += int(line)
        continue

    counter_max_calorie = max(counter_max_calorie, counter_current_elf)
    counter_current_elf = 0

print(counter_max_calorie)
file.close()

# part two
file = open("2022_2_AOC_input.txt")

first_elf = 0
second_elf = 0
third_elf = 0
counter_current_elf = 0
for line in file:
    if line != "\n" and line != "":
        counter_current_elf += int(line)
        continue

    if counter_current_elf > first_elf:
        third_elf = second_elf
        second_elf = first_elf
        first_elf = counter_current_elf

    elif counter_current_elf > second_elf:
        third_elf = second_elf
        second_elf = counter_current_elf

    elif counter_current_elf > third_elf:
        third_elf = counter_current_elf

    counter_current_elf = 0


answer = first_elf + second_elf + third_elf
print(answer)
file.close()
# 197736
# 34709588
