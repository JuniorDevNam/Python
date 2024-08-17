'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 9: Viết chương trình Python tính số lượng các số dương liên tiếp có tổng lớn nhất.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong = []
temp = []
for x in range(len(a)):
    if a[x] > 0:
        temp.append(a[x])
        if a[x] == a[-1]:
            if sum(temp) > sum(tong):
                tong = temp.copy()
    
    if a[x] < 0:
        if sum(temp) > sum(tong):
            tong = temp.copy()
        temp.clear()
print("Số lượng các số dương liên tiếp có tổng lớn nhất là {}".format(len(tong)))