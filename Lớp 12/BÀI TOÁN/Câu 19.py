'''
Bài 19: Viết chương trình Python xóa phần tử thứ k (k nhập từ bàn phím) trong danh sách.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
print("Danh sách a = {}".format(a))
print("Danh sách a chỉ có {} phần tử, hãy nhập số k trong khoảng 1 đến {}".format(len(a),len(a)))
k = int(input("Nhập số k: "))
xoa = a.copy()
xoa.pop(k-1)
print("Danh sách sau khi xóa phần tử thứ k = {}: {}".format(k,xoa))