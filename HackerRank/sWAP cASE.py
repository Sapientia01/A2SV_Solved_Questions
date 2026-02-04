def swap_case(s):
    chrs = list(s)
    
    for i,c in enumerate(chrs):
        if c.isalpha():
            if c.islower():
                chrs[i] = c.upper()
            else:
                chrs[i] = c.lower()
            
    return "".join(chrs)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)