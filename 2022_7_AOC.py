file = open("2022_7_AOC_input.txt").read()
file = file.split("\n")

d = dict()
s = ["/"]
for com in file:
    if not s[-1] in d.keys():
        d[s[-1]] = 0

    if com.startswith("$ cd /"):
        s = ["/"]
        continue

    if com.startswith("$ cd .."):
        s.pop()

    elif com.startswith("$ cd"):
        s.append(s[- 1] + com.replace("$ cd ", "") + "/")

    elif com[0].isdigit():
        i, *_ = com.split(" ")
        for e in s:
            d[e] += int(i)

ret = 0
for k, v in d.items():
    if v <= 100_000:
        ret += v

# part one
print("part one =", ret)

hard_drive_space = 70_000_000
freed_up_space = 30_000_000 - (hard_drive_space - d["/"])

dictSize = d["/"]
for k, v in d.items():
    if v >= freed_up_space:
        dictSize = min(dictSize, v)

# part two
print("part two =", dictSize)
