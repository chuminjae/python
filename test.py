c = [[0] * 10 for _ in range(10)]
for i in range(10):
    c[i]=list(map(int, input().split()))
i = 1
j = 1
while c[i][j] != 2:
    if(c[i][j] == 0):
        c[i][j] = 9
    if((i == 9 and j == 9) or (c[i][j + 1] == 1)and c[i+1][j] == 1):
        break
    if(c[i][j + 1] != 1):
        j += 1
        if(c[i][j] == 2):
            c[i][j] = 9
            break
    elif(c[i + 1][j] != 1):
        i += 1
        if(c[i][j] == 2):
            c[i][j] = 9
            break
for i in range(10):
    for j in range(10):
        print(c[i][j], end = " ")
    print("")
