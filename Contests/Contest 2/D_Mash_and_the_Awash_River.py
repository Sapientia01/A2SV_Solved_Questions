t  = int(input())
for _ in range(t):
    s = input()

    if ">*" in s or "*<" in s or "**" in s or "><" in s:
        print(-1)
        continue
    elif len(s) == 1:
        print(1)
        continue

    max_num = 0
    cur = 1
        
    for i in range(1,len(s)):
        if s[i] == "*":
            cur += 1
        elif s[i-1] == s[i]:
            cur += 1
        elif i > 0 and s[i-1] == "*":
            cur = 2
        else:
            cur = 1

        max_num = max(max_num, abs(cur))

    print(max_num)
        