'''
https://hnoj.edu.vn/problem/pa058
Một người nông dân nọ có một mảnh đất có dạng hình tứ giác lồi. Mảnh đất đó được trải trên mặt phẳng toạ độ Oxy với bốn đỉnh có toạ độ tương ứng theo chiều kim đồng hồ là 
A(xa,ya), B(xb, yb), C(xc, yc) và D(xd, yd). 
Bác nông dân cần biết diện tích của mảnh đất để tính toán lợi nhuận nhưng bác còn vướng bận công việc cày cấy.
Bạn hãy giúp bác nông dân nhé!
'''
xa, ya = map(float,input().split())
xb, yb = map(float,input().split())
xc, yc = map(float,input().split())
xd, yd = map(float,input().split())
#vecto AB
x_vtAB = xb - xa
y_vtAB = yb - ya
#vecto AD
x_vtAD = xd - xa
y_vtAD = yd - ya
#vecto CB
x_vtCB = xb - xc
y_vtCB = yb - yc
#vecto CD
x_vtCD = xd - xc
y_vtCD = yd - yc

#Dien tich tam giac ABD
ABD = abs((x_vtAB*y_vtAD)-(x_vtAD*y_vtAB))/2
#Dien tich tam giac CBD
CBD = abs((x_vtCB*y_vtCD)-(x_vtCD*y_vtCB))/2

#Dien tich hinh tu giac
kq = ABD + CBD

print(round(kq,3))