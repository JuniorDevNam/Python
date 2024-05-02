'''
Ý tưởng:
Duyệt từng ký tự trong chuỗi, xét xem liệu ký tự đó có trong khoảng từ A đến z.
Chuyển ký tự đó sang dạng mã unicode, sau đó cộng thêm 3
Chuyển lại từ unicode sang ký tự và in ra
'''

i = str(input("nhap: "))
f = ""
for x in i:
    if "A" <= x and x <= "z":
        f = f + chr(ord(x)+3)
    else:
        f = f + x

print(f)