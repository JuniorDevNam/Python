# Tìm tần suất xuất hiện của một ký tự trong một chuỗi.

chuoi = list(str(input("Nhập chuỗi: ")))
ky_tu = str(input("Nhập ký tự cần tìm trong chuỗi: "))
print(f"Tần suất xuất hiên ký tự {ky_tu} trong chuỗi là: {chuoi.count(ky_tu)}")