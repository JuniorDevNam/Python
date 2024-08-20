'''
Bài 14: Viết chương trình Python đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
x = int(input("Nhập giá trị X: "))
sl = 0
for i in a:
    if i == x:
        sl += 1
print(sl)