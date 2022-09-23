number = int(input())
d = {}
for i in range(number):
    words = input().split()
    word = words[0]
    definition = words[1:len(words) + 1]  #срез
    d[word] = definition
for i in range(int(input())):
    word = input()
    if word not in d:
        print('Нет в словаре')
    else:
        print(*d[word])
