'''
Ý tưởng:
Nhập vào họ và tên dưới dạng chuỗi
Sau đó tách các từ trong họ và tên rồi cho vào 1 danh sách
Truy xuất rồi in ra:
- Tên: phần từ đầu tiên của danh sách
- Đệm: các phần tử còn lại của danh sách sau khi đã loại bỏ phần tử đầu và cuối
- Tên: phần tử cuối của danh sách
'''

input = str(input("Họ và Tên: "))
t = []
t = input.split()
ho = t[0]
ten = t[-1]
del t[0]
del t[-1]
dem = " ".join(t)

print(input)
print(ho)
print(dem)
print(ten)
