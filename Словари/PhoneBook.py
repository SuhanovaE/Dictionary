d = {}
for i in range(int(input())):
    val, key = input().split()
    if key in d:
        d[key].append(val)
    else:
        d[key] = [val]
for i in range(int(input())):
    key = input()
    if key in d:
        print(*d[key])
    else:
        print('Нет в телефонной книге')
