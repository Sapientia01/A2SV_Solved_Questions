from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    t = sorted(input(),reverse=True)
    f = sorted(s,reverse=True)
    
   
    if  not (Counter(s) <= Counter(t)):
        print("Impossible")
    else:
        i = 0
        g = []

        for ch in t:
            if i < len(f) and ch == f[i]:
                i += 1
            else:
                g.append(ch)


        res = ''
        for ch in s:
            while g and g[-1] < ch:
                res += g.pop()

            res += ch

        while g:
           res += g.pop()

        print(res)