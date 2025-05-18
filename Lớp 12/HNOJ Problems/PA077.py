x = str(input())
y = str(input())
lx = [_ for _ in x]
ly = [i  for i in y]
if sorted(lx) == sorted(ly):
    print("YES")
else:
    print("NO")