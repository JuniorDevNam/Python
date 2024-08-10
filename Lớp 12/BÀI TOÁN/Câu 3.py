'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 3: Viết chương trình Python tính trung bình cộng của cả danh sách, 
trung bình cộng các phần tử dương trong danh sách.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
duong = [i for i in a if i > 0]
print("TBC của cả danh sách là: {}".format(sum(a)/len(a)))
print("TBC của các phần tử dương trong danh sách là: {}".format(sum(duong)/len(duong)))