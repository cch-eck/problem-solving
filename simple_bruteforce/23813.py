# import sys 

n = input()
print(sum(int(n[i]) for i in range(len(n))) * (int('1'*len(n))))
# print(sys.maxsize)