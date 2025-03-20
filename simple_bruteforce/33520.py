import sys
n = int(input())
chocobar1 = list()
chocobar2 = list()
for i in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    # 오름차순 정렬
    if a > b:
        a,b = b,a
    chocobar1.append(a)
    chocobar2.append(b)
    
print(max(chocobar1) * max(chocobar2))