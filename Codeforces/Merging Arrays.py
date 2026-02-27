# Question link:  https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int,input().split())
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

i = 0
j = 0

while i < len(nums1)  and j < len(nums2):
    if nums1[i] > nums2[j]:
        nums1.insert(i,nums2[j])
        i += 1
        j += 1
    else:
        i += 1

if j < len(nums2):
    nums1.extend(nums2[j:])


print( ' '.join(map(str,nums1)))