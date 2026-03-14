t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    min_len = n+1
    for i in range(n):
        if s[i] == "a":
            count = {"a":0, "b":0, "c":0}
            for j in range(i,min(i+10,n)):
                count[s[j]] += 1
                if count["a"] > count["b"] and count["a"] > count["c"] and sum(count.values()) > 1:
                    min_len = min(min_len, j-i+1)
                    break

    print(min_len if min_len < n+1 else -1)