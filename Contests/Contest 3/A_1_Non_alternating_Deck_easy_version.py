t = int(input())
for _ in range(t):
    n =  int(input()) 
    ab = [0,0]
    turn =  0
    cur = 1
    
    while n > 0:
        turn %= 2
        if  n > cur:
            ab[turn] += cur
            n -= cur
            cur += 4
            turn += 1
        else:
            ab[turn] += n
            n = 0
            cur += 4
            turn += 1

    print(*ab)