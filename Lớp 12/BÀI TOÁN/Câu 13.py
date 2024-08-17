'''

Bài 13: Viết chương trình Python tìm đoạn con có các số hạng dương liên tiếp có tổng lớn nhất.
(Nếu có nhiều đoạn con thoả mãn thì đưa ra màn hình: Số đoạn con thoả mãn và các đoạn con đó).
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
def max_tong(a):
    tong = []
    temp = []
    for x in a:
        if x > 0:
            temp.append(x)
            print(temp)
            if x == a[-1]:
                if sum(temp) > sum(tong):
                    tong = temp.copy()
        
        if x < 0:
            if sum(temp) > sum(tong):
                tong = temp.copy()
                print(tong)
            temp.clear()
    return sum(tong)
temp = []
ds = []
for x in range(len(a)):
    if a[x] > 0:
        temp.append(a[x])
    if a[x] < 0:
        if sum(temp) == max_tong(a):
            ds.append(temp.copy())
        temp.clear()

print("Các số hạng dương liên tiếp có tổng lớn nhất là {} gồm {} đoạn con thỏa mãn như sau: {}".format(max_tong(a),len(ds),ds))