# n, k = map(int,input().split())
# nums = list(map(int,input().split()))
nums = [1,4,7,3,7,2,1]
# nums = [3,1,2,4]

n = len(nums)

prev_smaller = [-1]*n
stack = []
for i in range(n):
    while stack and nums[i] <= nums[stack[-1]]:
        stack.pop()

    if stack:
        prev_smaller[i] = stack[-1]

    stack.append(i)

for i in range(n):
    prev_smaller[i] = i+1 if prev_smaller[i] == -1 else i - prev_smaller[i]


next_smaller = [-1] * n
stack = []
for i in range(n):
    while stack and nums[i] < nums[stack[-1]]:
        next_smaller[stack.pop()] = i

    stack.append(i)

for i in range(n):
    next_smaller[i] = n-i if next_smaller[i] == -1 else next_smaller[i] - i






print(next_smaller)
print(prev_smaller)
print(sum(next_smaller[i]*prev_smaller[i]*nums[i] for i in range(n)))

# print([nums[i] if i != -1 else -1 for i in next_smaller ])