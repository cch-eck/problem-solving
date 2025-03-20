N = int(input())
A = list(map(int, input().split()))

first, last = A[0], A[-1]
for B in range(N-1):
    if abs(first-last) - (N-3) + 2*B >= -1:
        break
A, B = min(B, N-3-B), max(B, N-3-B)
first, last = min(first, last), max(first, last)
print(max(first-A-1, last-B-1))