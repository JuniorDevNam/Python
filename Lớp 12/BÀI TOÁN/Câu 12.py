'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 12: Viết chương trình Python tìm vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

def duong_max_ptu(a):
    tong = []
    temp = []
    for x in range(len(a)):
        if a[x] > 0:
            temp.append(a[x])
        if a[x] < 0:
            if sum(temp) > sum(tong):
                tong = temp.copy()
            temp.clear()
    return len(tong)
temp = []
ds = []
for x in range(len(a)):
    if a[x] > 0:
        temp.append(a[x])
    if a[x] < 0:
        if len(temp) == duong_max_ptu(a):
            ds.append(temp.copy())
        temp.clear()

kq = []
for y in range(len(a)):
    for i in range(len(ds)):
        if a[y] == ds[i][0]:
            kq.append(y+1)

print("Vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất là: {}".format(", ".join(str(x) for x in kq)))
        
