t = int(input())
for _ in range(t):
    n =  int(input()) 
    s = input()
    m= len(s)
    if len(s) < n:
        print("YES")

    else:
        for i in range(n-1):
            if s[i:i+2] in s[:i]:
                print("YES")
                break

        else:
            print("NO")