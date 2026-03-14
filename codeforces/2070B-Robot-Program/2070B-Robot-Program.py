t = int(input())
for _ in range(t):
    n, x , k = list(map(int,input().split()))
    s = input()
    zeros = i = 0
    for ch in s:
        k -= 1
        if ch == "L":
            x -= 1
        else:
            x += 1
        if x == 0:
            zeros += 1
            break

    if zeros == 1 and n > 1:

        x = -1 if s[0] == "L" else 1
        i = 1
        
        for ch in s[1:]:
            i += 1
            if ch == "L":
                x -= 1
            else:
                x += 1
            if x == 0:
                break
        if x == 0:
            zeros += (k//i)
        
    print(zeros)