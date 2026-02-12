from collections import defaultdict

def solve(s,n):
    if "aa" in s:
        return 2
    elif s.count("a") < 2:
        return -1
    
    a = []
    min_len = n

    for i,ch in enumerate(s):
        if ch == "a":
            a.append(i)

    for index in a:
        i = index
        counts = {}
        found = False

        while i < n and not found :
            cur_len = i - index + 1

            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1


            if "a" in counts and "b" in counts and "c" in counts and cur_len > 3:
                if counts["a"] > counts["b"] and counts["a"] > counts["c"]:
                    found = True
                    break
            
            elif "a" in counts and "b" in counts and cur_len > 2:
                if counts["a"] > counts["b"]:
                    found = True
                    break 

            elif "a" in counts and "c" in counts and cur_len > 2:
                if counts["a"] > counts["c"]:
                    found = True
                    break 


            i += 1



        if found:
            # print(min_len,  i - index + 1 ) 
            min_len = min(min_len,  cur_len)    

    return min_len




t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(s,n))
