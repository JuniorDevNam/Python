'''
Cho hai điểm A(xa;ya) và B(xb;yb) trên mặt phẳng toạ độ Oxy.
Hãy tính khoảng cách giữa hai điểm A và B.
https://hnoj.edu.vn/problem/pa056
'''
xa, ya, xb, yb = map(float, input().split())
x_vectoAB = xb - xa
y_vectoAB = yb - ya
do_dai_vecto = ((x_vectoAB**2) + (y_vectoAB**2))**0.5
print(round(do_dai_vecto,3))
