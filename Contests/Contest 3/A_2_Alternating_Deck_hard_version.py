from math import ceil

t = int(input())
for _ in range(t):
    n =  int(input()) 
    ab = [[0,0],[0,0]]
    turn =  0
    index = 0
    cur = 1
    while n > 0:
        turn %= 2
        cur = min(cur, n)

        black = 0
        white = 0
        if index % 2 == 0:
            white = ceil(cur/2)
            black = cur//2
        else:
            black = ceil(cur/2)
            white = cur//2

        ab[turn][0] += white
        ab[turn][1] += black

        index += cur
        n -= cur
        cur += 4
        turn += 1

    print(*ab[0], *ab[1])