'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 8: Viết chương trình Python tính số lượng các số dương liên tiếp nhiều nhất.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
s = 0
for x in a:
    if x > 0:
        s += 1
    else:
        s -= s
print("Số lượng các số dương liên tiếp nhiều nhất là {}".format(s))