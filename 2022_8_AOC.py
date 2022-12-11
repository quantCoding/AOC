file = open("2022_8_AOC_input.txt").read()

l = []
for r, line in enumerate(file.split("\n")):
    l.append(list(line))

s = set()
visible = 0
visible_trees = 0
for r in range(len(l)):
    for c in range(len(l[r])):

        sight_left = all(l[r][x] < l[r][c] for x in range(c))
        sight_right = all(l[r][x] < l[r][c] for x in range(c + 1, len(l[r])))
        sight_up = all(l[x][c] < l[r][c] for x in range(r))
        sight_down = all(l[x][c] < l[r][c] for x in range(r + 1, len(l)))

        if sight_left or sight_right or sight_up or sight_down and (r, c) not in s:
            s.add((r, c))
            visible += 1

        visible_left = 0
        for x in range(c - 1, -1, -1):
            visible_left += 1
            if l[r][x] >= l[r][c]:
                break

        visible_right = 0
        for x in range(c + 1, len(l[r])):
            visible_right += 1
            if l[r][x] >= l[r][c]:
                break

        visible_up = 0
        for x in range(r - 1, -1, -1):
            visible_up += 1
            if l[x][c] >= l[r][c]:
                break

        visible_down = 0
        for x in range(r + 1, len(l)):
            visible_down += 1
            if l[x][c] >= l[r][c]:
                break

        # print (r,c,visible_up,visible_right,visible_down, visible_left)
        visible_trees = max(visible_trees, visible_up * visible_down * visible_right * visible_left)

print(visible)
print(visible_trees)
