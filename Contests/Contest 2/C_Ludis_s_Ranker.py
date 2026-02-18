n = int(input())
nums = list(map(int,input().split()))
order = sorted(nums,reverse= True)
highers = {}
count = 0
cur = order[0]
highers[cur] = 0

for index,num in enumerate(order):
    if num != cur:
        highers[num] = index
        cur = num

print(*[highers[num] +1 for num in nums])