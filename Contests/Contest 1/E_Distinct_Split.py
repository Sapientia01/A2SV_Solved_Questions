from collections import Counter
t  = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    left = Counter(s[:1])
    right = Counter(s[1:])
    max_sum = len(left) + len(right)

    for i in range(1,n-1):
        if s[i] not in left:
            left[s[i]] = 1

        if right[s[i]] > 1:
            right[s[i]] -= 1
        else:
            del right[s[i]]

        cur_sum = len(left) + len(right)
        max_sum = max(cur_sum,max_sum)

    print(max_sum)


