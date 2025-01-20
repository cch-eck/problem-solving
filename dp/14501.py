# dp table: i일차의 최대 수익을 D[i]라고 하자.
import sys
N = int(input())
schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# schedule = (T: 상담 일수, P: 금액)
D = [0 for _ in range(N+1)]

for day in range(N):
    T, P = schedule[day]
    # 시간 내에 상담을 할 수 있으면 한다.
    if day + T <= N:
        D[day+T] = max(D[day+T], D[day]+P)
    # 상담을 안하는 게 나은지 확인한다(?)
    if day + 1 <= N:
        D[day+1] = max(D[day+1], D[day])

print(D[N])