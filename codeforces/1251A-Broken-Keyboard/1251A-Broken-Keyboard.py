t = int(input())

for _ in range(t):
    s =input()
    n = len(s)
    res = set('')
    left = 0
    right = 1
    

    while left < n and right < n:
        while right < n and s[left] == s[right]:
            right += 1

        if (right-left) % 2 == 1:
            res.add(s[left])
        
        left = right



    if len(s) == 1:
        res.add(s)


    res = sorted(list(res))
    if len(res) > 0:
        ans = ''
        for i in res:
            ans += i
        print(ans)
    else:
        print()