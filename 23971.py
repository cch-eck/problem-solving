def roundup(n: int) -> int:
    if n == n//1:
        return n//1
    else:
        return n//1+1
    
# H, W, N, M
h, w, n, m = map(int, input().split())
ans = int(roundup(h/(n+1)) * roundup(w/(m+1)))
print(ans)