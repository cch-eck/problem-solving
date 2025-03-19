n= int(input())
D=[0 for _ in range(n+1)]

D[1] = 1
D[2] = 2
'''
D[3] = 3
D[4] = 5
D[5] = 8
'''
for i in range(3,n+1):
    D[i] = (D[i-1]+D[i-2])%10007
print(D[i])