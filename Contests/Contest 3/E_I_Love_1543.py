t = int(input())
for _ in range(t):
    n,m  =  list(map(int,input().split()))
    square = []

    for i in range(n):
        row = list(map(int,input()))
        square.append(row)

    layers = min(n,m) //2
    count = 0

    for i in range(layers):
        cur_layer = []

        # top 
        cur_layer.extend(square.pop(0))

        # right
        for i in range(len(square)):
            cur_layer.append(square[i].pop())
        
        # bottom
        cur_layer.extend(square.pop(-1)[::-1])

        # left
        for i in range(len(square)):
            cur_layer.append(square[len(square) - 1- i].pop(0))
        
        # top 3 numbers
        cur_layer.extend(cur_layer[:3])

        cur_layer = "".join(map(str,cur_layer))
        count += cur_layer.count("1543")

    print(count)