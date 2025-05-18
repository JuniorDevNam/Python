a, b, c = map(int, input().split())

ptb = -(a + b)
ptc = a * b
delta = ptb**2 - 4 * 1 * ptc

nghiem = set()

if delta > 0:
    x1 = (a + b + delta**0.5) / 2
    x2 = (a + b - delta**0.5) / 2
    nghiem.add(x1)
    nghiem.add(x2)
elif delta == 0:
    x1 = (a + b) / 2
    nghiem.add(x1)

nghiem.add(c)

print(len(nghiem))