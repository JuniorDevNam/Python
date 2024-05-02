can = float(input("Nhập số khối lượng cam: "))
while can < 0:
    can = float(input("Không hợp lệ, xin nhập lại: "))
tien = 0
if can < 5:
    tien = 12000*can
else:
    if can >= 5:
        tien = 10000*can
print("Số tiền cho",can,"kg cam là:",tien)