def solve():
    n, q = map(int, input().split())
    h = list(map(int, input().split()))

    for _ in range(q):
        l, r = map(int, input().split())
        f = [x for x in h if l <= x <= r]
        d = sum(abs(f[i] - f[i-1]) for i in range(1, len(f))) if len(f) > 1 else 0
        print(d)

solve()