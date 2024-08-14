'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 12: Viết chương trình Python tìm vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong = 0
temp = []
vi_tri = []
temp2 = 0
for x in range(len(a)):
    if a[x] > 0:
        temp.append(a[x])
    print(temp)
    if a[x] < 0:
        if len(temp) > temp2:
            temp2 = len(temp)
            vi_tri.append(temp)
        temp.clear()
print(vi_tri)
print("Vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất là: {}".format(vi_tri[x][0] for x in range(len(vi_tri))))
        
