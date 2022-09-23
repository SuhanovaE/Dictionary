line = input().split()
d1 = {}
d2 = {}
for i in range(len(line)):
    if line[i] not in d1:
        d2.append("1")
        d1.append(line[i])
    else:
        d2.append(str(d1.count(line[i]) + 1))
        d1.append(line[i])
print(" ".join(d2))
