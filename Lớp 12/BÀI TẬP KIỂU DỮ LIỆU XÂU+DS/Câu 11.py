# Viết chương trình nhập vào dãy các số nguyên bất kỳ, 
# kiểm tra và xuất ra màn hình xem dãy số đó có tạo thành cấp số cộng hay không

#test:
# csc: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48
# ko phải csc: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

ds = list(map(int,input("Nhập dãy các số nguyên bất kỳ đuọc cách nhau bởi dấu phẩy: ").split(",")))
for i in range(len(ds)-3):
    if not ds[i+3] - ds[i+2] == ds[i+1] - ds[i]:
        print("Không phải cấp số cộng.")
        break
else:
    print("Là cấp số cộng")