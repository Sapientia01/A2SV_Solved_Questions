def sort(arr, n, t):
    nums = arr.copy()
    opr = []

    for j in range(n - 1):
        i = j
        while i >= 0 and nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            opr.append([t, i + 1])
            i -= 1

    if t == 1:
        nums = [x if x <= n else x - 2 * n for x in nums]
    else:
        nums = [x if x <= 2 * n else x - 2 * n for x in nums]

    return nums, opr


def arrange(arr, n, pattern):
    nums = arr.copy()
    index = [-1] * (2 * n + 1)
    opr = []
    member = []
    not_memb = []

    for i, num in enumerate(nums):
        index[num] = i
        if num > n:
            not_memb.append(num)
        else:
            member.append(num)

    member.reverse()
    not_memb.reverse()

    i = 0
    while i < n:
        if (nums[i] <= n and pattern[i]) or (nums[i] > n and not pattern[i]):
            if member and nums[i] == member[-1]:
                member.pop()
            elif not_memb and nums[i] == not_memb[-1]:
                not_memb.pop()
            i += 1

        elif nums[i] <= n and not_memb:
            x = not_memb.pop()
            j = index[x]

            while j > i:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                index[nums[j]] = j
                index[nums[j - 1]] = j - 1
                opr.append([1, j])
                j -= 1

        elif nums[i] > n and member:
            x = member.pop()
            j = index[x]

            while j > i:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                index[nums[j]] = j
                index[nums[j - 1]] = j - 1
                opr.append([1, j])
                j -= 1

    return nums, opr


t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    total_opr = []
    pattern = [x > n for x in nums2]

    nums1, opr1 = arrange(nums1, n, pattern)
    total_opr.extend(opr1)

    for i in range(n):
        if not pattern[i]:
            nums1[i], nums2[i] = nums2[i], nums1[i]
            total_opr.append([3, i + 1])

    nums1, opr1 = sort(nums1, n, 1)
    nums2, opr2 = sort(nums2, n, 2)

    total_opr.extend(opr1)
    total_opr.extend(opr2)

    print(len(total_opr))
    for op in total_opr:
        print(*op)



    








# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

#     ops = []

#     # ensure a[i] < b[i]
#     for i in range(n):
#         if a[i] > b[i]:
#             a[i], b[i] = b[i], a[i]
#             ops.append((3, i+1))

#     # sort a
#     for _ in range(n):
#         for i in range(n-1):
#             if a[i] > a[i+1]:
#                 a[i], a[i+1] = a[i+1], a[i]
#                 ops.append((1, i+1))

#     # sort b
#     for _ in range(n):
#         for i in range(n-1):
#             if b[i] > b[i+1]:
#                 b[i], b[i+1] = b[i+1], b[i]
#                 ops.append((2, i+1))

#     # fix ai < bi again if needed
#     for i in range(n):
#         if a[i] > b[i]:
#             a[i], b[i] = b[i], a[i]
#             ops.append((3, i+1))

#     print(len(ops))
#     for x, y in ops:
#         print(x, y)