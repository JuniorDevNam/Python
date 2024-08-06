# Viết chương trình nhập vào dãy các số bất kỳ, tìm số lớn nhất trong dãy số đó và xuất ra màn hình?

#test: 1, 4, 2, 6, 3, 5, 7, 13, 23, 55, 73, 9, 21
#ket qua:

ds = list(map(int,input("Nhập dãy số bất kỳ cách nhau bởi dấu phẩy: ").split(",")))
print(max(ds))