#  Question link : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem


n = int(input())
phones = {}

for _ in range(n):
    name, phone = input().split()
    phones[name] = phone
    
while True:
    try:
        name = input()
        if name in phones:
            print(name + "=" + phones[name])
        else:
            print("Not found")
    except Exception:
        break