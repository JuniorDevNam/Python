hs = int(input("Nhập số học sinh trong lớp: "))
ds_lop = []
for i in range(hs):
    ds_lop.append(input("Nhập họ tên học sinh thứ "+str(i+1)+": "))
if hs > 10:
    n = 1
    count = 0
    while n <= hs:
        count = count + 1
        if count%10 == 0:
            print(ds_lop[count])
        else:
            print("Danh sách lớp học:",ds_lop, end = " ")
        n = n + 1
hs_huong = "Hương"
so_hs_huong = 0
for x in ds_lop:
    if hs_huong in x:
        so_hs_huong += 1

print("Số học sinh tên Hương có trong danh sách học sinh là:",so_hs_huong)