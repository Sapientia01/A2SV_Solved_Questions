n, k = map(int, input().split())
nums = list(map(int, input().split()))

diff = []
for i in range(1, n):
    diff.append(nums[i] - nums[i-1])

diff.sort()

print(sum(diff[:n-k]))