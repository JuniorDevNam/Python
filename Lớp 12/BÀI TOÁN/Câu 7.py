'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 7: Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách
và các vị trí của các phần tử đạt giá trị lớn nhì.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
so_nhi = 0
for x in a:
    if x > so_nhi:
        if x != max(a):
            so_nhi = x
vi_tri = [i+1 for i in range(len(a)) if a[i] == so_nhi]
print("Phần tử lớn thứ nhì của danh sách là {} và các vị trí của các phần tử đó là {}".format(so_nhi,", ".join(str(x) for x in vi_tri)))