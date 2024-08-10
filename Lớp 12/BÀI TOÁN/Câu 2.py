'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 2: Viết chương trình Python đếm số lượng các số hạng dương và tổng của các số hạng dương.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
ds = [x for x in a if x > 0]
print("Số lượng các số hạng dương trong danh sách là: {}".format(len(ds)))
print("Tổng các số hạng dương trong danh sách là: {}".format(sum(ds)))