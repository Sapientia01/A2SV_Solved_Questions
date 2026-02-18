t = int(input())
for _ in range(t):
    m, s = list(map(int,input().split()))
    nums = set(map(int,input().split()))
    max_num = max(nums)
    cur = 0
    added = 0

    while s > 0:
        cur += 1

        if cur not in nums:
            added += 1
            s -= cur
            

    if s == 0 and m + added == max(cur, max_num):
        print("YES")
    else:
        print("NO")