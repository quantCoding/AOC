file = open("2022_2_AOC_input.txt").read()
list = []
for line in file.split("\n"):
    list.append(line.strip())

# part one

# win cases
# b z = -1
# a y = -1
# c x = +2

score = 0
for line in list:
    opponent, strategy_guid = line.strip().split(" ")
    outcome = ord(opponent) - (ord(strategy_guid) - ord("X") + ord("A"))
    if outcome == 0:
        score += 3 + ord(strategy_guid) + 1 - ord("X")
        continue

    if outcome == -1 or outcome == 2:
        score += 6 + ord(strategy_guid) + 1 - ord("X")
        continue

    score += ord(strategy_guid) + 1 - ord("X")

print(score)
score = 0

# part two
win_grid = ["A", "B", "C", "A"]
lose_grid = ["C", "B", "A", "C"]

for line in list:
    opponent, outcome = line.strip().split(" ")
    if outcome == "Y":
        score += 3 + ord(opponent) - ord("A") + 1
        continue

    if outcome == "X":
        score += ord(lose_grid[lose_grid.index(opponent) + 1]) - ord("A") + 1
        continue

    score += 6 + ord(win_grid[win_grid.index(opponent) + 1]) - ord("A") + 1

print(score)
