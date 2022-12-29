input = [list(x.strip()) for x in open("2022_24_AOC_input.txt")]

# bord definitions
box_up = 1
box_down = len(input) - 2
box_left = 1
box_right = len(input[0]) - 2

def print_field(blizzards):
    for row in range(1, box_down + 1):
        temp = ""
        for column in range(1, box_right + 1):
            directions = [d for r, c, d in blizzards if row == r and column == c]
            temp += directions.pop() if len(directions) == 1 else "." if len(directions) == 0 else str(len(directions))
        if row == 1:
            print("#" * (box_right + 2))
        print("#", temp, "#", sep="")
        if row == box_down:
            print("#" * (box_right + 2))

def move_pos(blizzard, minute):
    row, column, direction = blizzard
    if direction == "<":  # left
        column -= minute
    elif direction == ">":  # right
        column += minute
    elif direction == "^":  # up
        row -= minute
    elif direction == "v":  # down
        row += minute

    row = (row - 1) % box_down + 1
    column = (column - 1) % box_right + 1
    return row, column

blizzard_forecast = dict()
def for_minute(blizzards, minute):
    if minute in blizzard_forecast:
        return blizzard_forecast[minute]

    ret = set()
    for blizzard in blizzards:
        ret.add(move_pos(blizzard, minute))

    blizzard_forecast[minute] = ret
    return ret

def bfs(blizzards, start, finish, start_minute):
    visited = set()
    queue = [(start, start_minute)]
    while queue:

        pos_current, minute = queue.pop(0)
        if (pos_current, minute) in visited:
            continue

        visited.add((pos_current, minute))

        if pos_current == finish:
            return minute

        if pos_current in for_minute(blizzards, minute):
            continue

        row, col = pos_current
        if (row, col) != start and (row < box_up or row > box_down or col < box_left or col > box_right):
            continue

        queue.append(((row, col), minute + 1))
        queue.append(((row + 1, col), minute + 1))
        queue.append(((row - 1, col), minute + 1))
        queue.append(((row, col + 1), minute + 1))
        queue.append(((row, col - 1), minute + 1))

    return "NO SOLUTION FOUND"


# for i in range(10):
#     print ("step",i)
#     test = for_minute(poss, i)
#     #print_field(poss)
#     print()
#     print_field(test)


# print(poss)
# print(test)

start_pos = (0, 1)
end_pos = (box_down + 1, box_right)

blizzards = []
for row in range(len(input)):
    for col in range(len(input[row])):
        if input[row][col] in "<>^v":
            blizzards.append((row, col, input[row][col]))

part_one = bfs(blizzards, start_pos, end_pos, 0)
backpack = bfs(blizzards, end_pos, start_pos, part_one)
part_two = bfs(blizzards, start_pos, end_pos, backpack)

# part one 301
# part two 859
print("part one", part_one, "backpack", backpack, "part two", part_two, sep="\n")
