#  B

t  = int(input())
for _ in range(t):
    num = input()
    n = len(num)
    a = num[:1]
    b = num[1:]
    i = 1
    found = False
    while not found and i < n:
        a,b = int(a), int(b)
    
        if b > a and len(str(a)) + len(str(b)) == len(num):
            found = True
        else:
            i += 1
            a, b = num[:i], num[i:]

    if found:
        print(a,b)
    else:
        print(-1)