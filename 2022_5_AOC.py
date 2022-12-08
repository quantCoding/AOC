file = open("2022_5_AOC_input.txt").read()
len = 9

crs, mvs = file.split("\n\n")
crs = crs[1::4]

list = [[] for _ in range(len)]

for i, cr in enumerate(crs):
    if cr == " " or cr.isdigit():
        continue

    list[i % len] = [cr] + list[i % len]

for mv in mvs.split("\n"):
    n, f, t = map(int, mv.split(" ")[1::2])
    
    # part one
    #list[t - 1] += list[f - 1][-n:][::-1]
    
    # part two
    list[t - 1] += list[f - 1][-n:]
    
    list[f - 1] = list[f - 1][:-n]

print("".join([i[-1] for i in list]))