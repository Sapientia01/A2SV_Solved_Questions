# https://codeforces.com/problemset/problem/1165/B

n = int(input())
nums = sorted(map(int,input().split()))
cur = 1
res = 0

for num in nums:
    if num >= cur:
        res += 1
        cur += 1
print(res)