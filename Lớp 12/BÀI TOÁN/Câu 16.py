'''
Bài 16: Viết chương trình Python tìm số phần tử là dương 
và là số nguyên tố của danh sách và vị trí của nó trong danh sách.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
def snt(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True
so_nt = [x for x in a if snt(x)]
print(so_nt)
vi_tri = [i+1 for i in range(len(a)) if snt(a[i])]
print(vi_tri)
print("Các số phần tử là dương và là số nguyên tố của danh sách là {} năm ở các vị trí {} trong danh sách".format(", ".join(str(x) for x in so_nt),", ".join(str(i) for i in vi_tri)))