'''
Bài 17: Viết chương trình Python chèn một số m (m nhập vào từ bàn phím )
vào đầu danh sách, cuối danh sách và vị trí thứ 5 của danh sách.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
m = int(input("Nhập số m: "))
print("Danh sách a = {}".format(a))
dau, cuoi, nam = a.copy(), a.copy(), a.copy()
dau.insert(0,m)
cuoi.append(m)
nam.insert(4,m)
print("Chèn m vào đầu danh sách: {}".format(dau))
print("Chèn m vào cuối danh sách: {}".format(cuoi))
print("Chèn m vào vị trí thứ 5 của danh sách: {}".format(nam))
