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
    tong = 0
    temp = 0
    so_lg = 0
    temp2 = 0
    for x in range(len(a)):
        if a[x] > 0:
            temp += a[x]
            temp2 += 1
        if a[x] < 0:
            if temp > tong:
                tong -= tong
                tong += temp
                so_lg -= so_lg
                so_lg += temp2
            temp -= temp
            temp2 -= temp2
    return so_lg
tong = 0
temp = []
vi_tri = []
temp2 = []
for x in range(len(a)):
    if a[x] > 0:
        temp.append(a[x])
    print(temp)
    if a[x] < 0:
        if len(temp) > len(temp2) or (len(temp) == len(temp2) == duong_max_ptu(a)):
            temp2 = temp.copy()
            vi_tri.append(temp2)
            print(vi_tri)
        temp.clear()

kq = []
for i in range(len(vi_tri)):
    kq.append(vi_tri[i][0])

print("Vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất là: {}".format(kq))
        
