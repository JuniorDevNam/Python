'''
Bài 15: Viết chương trình Python chuyển các phần tử dương của danh sách lên đầu danh sách và in danh sách ra màn hình.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
ds = []
for i in a:
    if i > 0:
        ds.append(i)
for x in a:
    if x < 0:
        ds.append(x)
print(ds)