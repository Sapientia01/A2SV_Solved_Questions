n, k = map(int,input().split())
nums = list(map(int,input().split()))
res = 0
for num in nums:
    if num > 0 and num >= nums[k-1]:
        res += 1

print(res)
