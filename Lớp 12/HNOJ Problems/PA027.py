a = int(input())
b = int(input())
c = int(input())
d = int(input())
#------------------------------------
#Cách 1
ab = [x for x in range(a,b+1)]
cd = [y for y in range(c,d+1)]

if list( set(ab) & set(cd) ) != []:
    print("YES")
else:
    print("NO")

#------------------------------------
#Cách 2
if b < c or d < a:
    print("NO")
elif d >= a or b >= c:
    print("YES")