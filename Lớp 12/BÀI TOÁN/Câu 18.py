'''
Bài 18: Viết chương trình Python chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
ds = [1,2,3]
print("Danh sách a = {}".format(a))
dau, cuoi, nam = a.copy(), a.copy(), a.copy()

# Nếu theo cách này, sử dụng hàm insert
#  thì danh sách chèn vào sẽ chỉ được tính là 1 phần tử trong list a

# Có cách nào khăc phục và thay thế được hàm insert không thầy?

dau.insert(0,ds)
#cuoi.append(ds) #không dùng vì nó cũng giống insert, nó sẽ chèn danh sách [1,2,3] dưới dạng
                    # chỉ là 1 phần tử con trong list a, không phải 3 phần tử con
                    # 1, 2, 3 trong list a
cuoi.extend(ds)
nam.insert(4,ds)
print("Chèn danh sách {} vào đầu danh sách: {}".format(ds,dau))
print("Chèn {} vào cuối danh sách: {}".format(ds,cuoi))
print("Chèn {} vào vị trí thứ 5 của danh sách: {}".format(ds,nam))

