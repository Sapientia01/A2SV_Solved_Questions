t = int(input())
for _ in range(t):
    n = int(input())
    square = []

    for i in range(n):
        row = list(map(int,input()))
        square.append(row)

    opr = 0
    n -= 1
    
    for row in range(n+1):
        for col in range(n+1):
            ones = sum([square[row][col], square[col][n-row], square[n-row][n-col],square[n-col][row]])
            zeros = 4 - ones
            
            opr += min(zeros,ones)

    print(opr//4)