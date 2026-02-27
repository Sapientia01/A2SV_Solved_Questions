# Question link:  https://codeforces.com/problemset/problem/263/A

for i in range(5):
    row = "".join(input().split())
    one = row.find("1")
    if one > -1:
        print(abs(2-one) + abs(2-i))