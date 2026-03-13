t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    casidos = [list(map(int,input().split())) for _ in range(n)]
    casidos = sorted(casidos, key = lambda x: [x[0], x[2]])

    for l,r, p in casidos:
        if l <= k and k <= r:
            k = max(k,p)
            
    print(k)