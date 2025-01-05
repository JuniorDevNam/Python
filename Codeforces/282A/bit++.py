#Accepted

n = int(input())
bit = [str(input()) for _ in range(n)]
plus = ['X++', '+X+', '++X']
minus = ['X--', '-X-', '--X']
var = 0
for b in bit:
    if b in plus:
        var += 1
    if b in minus:
        var -= 1
print(var)