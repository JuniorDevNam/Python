'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 4: Viết chương trình Python tìm vị trí của phần tử âm đầu tiên trong danh sách.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
for i in range(len(a)):
    if a[i] < 0:
        print("Vị trí phần tử âm đầu tiên trong danh sách là {}".format(i+1))
        break