'''
Bài 7: Viết chương trình tính điểm trung bình 3 môn Toán, Lý , Hoá theo hệ số 2,1,1 sau đó xếp loại như sau:
a. Loại Giỏi : ĐTB >= 8.0 và không có môn nào dưới 6,5
b. Loại Khá : 6.5=<ĐTB < 8.0 và không có môn nào dưới 5
c. Loại Trung bình : 5.0 =<ĐTB < 6.5 và không có môn nào dưới 3.5
d. Loại Yếu : Còn lại.
'''
toan = float(input("Nhập số điểm môn Toán: "))
ly = float(input("Nhập số điểm môn Lý: "))
hoa = float(input("Nhập số điểm môn Hóa: "))
dtb = (toan*2 + ly + hoa)/4
if dtb >= 8 and toan > 6.5 and ly > 6.5 and hoa > 6.5:
    print("Học sinh Giỏi")
elif 6.5 <= dtb < 8 and toan > 5 and ly > 5 and hoa > 5:
    print("Học sinh Khá")
elif 5 <= dtb < 6.5 and toan > 3.5 and ly > 3.5 and hoa > 3.5:
    print("Học sinh Trung Bình")
else:
    print("Học sinh Yếu")