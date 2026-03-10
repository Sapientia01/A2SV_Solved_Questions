# https://codeforces.com/contest/710/problem/B

n = int(input())
nums = sorted(map(int,input().split()))
prev = 0
cur_p = nums[0]
for num in nums:
    prev += abs(num - nums[0])

cur = prev
for i in range(1,n):
    x = abs(nums[i-1] - nums[i])
    cur = cur - x  * (n-i-1)
    cur += x * (i-1)
    
    if cur < prev:
        cur_p = nums[i]
    prev = cur

print(cur_p)