from collections import Counter

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    c = input()
    chars1 = Counter(a+c)
    chars2 = Counter(b)
    pos = True
    i = 0
    j = 0


    while i < len(a) and j < len(b):
        if b[j] == a[i]:
            j += 1
            i += 1
        else:
            j += 1


    if i < len(a):
        pos = False


    if pos and chars2 <= chars1:
        print("YES")
    else:
        print("NO")