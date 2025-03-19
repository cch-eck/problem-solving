# 시간 제한이 빡세니까 dp를 사용해야 함
X = int(input())
D = [0 for _ in range(X+1)]

if X==1:
    print(0)
elif X<4:
    print(1)
else:
    D[0] = 0
    D[1] = 0
    D[2] = 1
    D[3] = 1

    for i in range(4, X+1):
        if i%6 == 0:
            D[i] = min(D[i//2]+1, D[i//3]+1, D[i-1]+1)
        elif i%3 == 0:
            D[i] = min(D[i//3]+1, D[i-1]+1)
        elif i%2 == 0:
            D[i] = min(D[i//2]+1, D[i-1]+1)
        else:
            D[i] = D[i-1]+1
    print(D[X])
    
