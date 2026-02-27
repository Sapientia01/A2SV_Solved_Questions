# Question link:  https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int,input().split())
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
result = []

left= 0
right = 0

while right < m:
    while left < n and nums1[left] < nums2[right]:
        left += 1
    result.append(left)

    right += 1


print(*result)