n = int(input())
stair = []
stair.append(0) 
for _ in range(n):
    stair.append(int(input())) 
D = [0 for _ in range(n+1)]

# 점화식 정의: D[i] = i번째 
D[0] = 0
# D[3] = max(D[1]+stair[3], D[0]+stair[2]+stair[3])
if n==1:
    print(stair[1])
elif n==2:
    print(stair[1]+stair[2])
else:
    D[1] = stair[1]
    D[2] = stair[1]+stair[2]
    for i in range(3, n+1):
        D[i] = max(D[i-2]+stair[i], D[i-3]+stair[i-1]+stair[i])
    print(D[n])