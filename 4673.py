def d(n):
    return n+sum(int(i) for i in str(n))

not_self_nums = set()
for n in range(1,10000):
    not_self_nums.add(d(n))

all_nums = set()
for i in range(1,10000):
    all_nums.add(i)

self_nums = list(all_nums - not_self_nums)
self_nums.sort()
for i in self_nums:
    print(i)