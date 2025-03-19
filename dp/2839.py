# 3, 5
N = int(input())
D = [-1 for _ in range(N+1)]
D[0] = 0
if N>=5:
    D[3], D[5]= 1, 1
elif N>=3:
    D[3] = 1
    
for i in range(6, N+1):
    if D[i-5] > 0:
        D[i] = D[i-5] + 1
    elif D[i-3] > 0:
        D[i] = D[i-3] + 1
print(D[N])
# for i in range(1,N+1):
#     print(f"D[{i}]:", D[i])