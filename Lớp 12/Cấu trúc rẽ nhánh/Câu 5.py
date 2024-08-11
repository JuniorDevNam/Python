# Bài 5: Viết chương trình giải phương trình bậc 1: ax+b=0
a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))

def pt_bac_1(a,b):
    if a == b:
        return -1
    else:
        return -b/a
print("x là:",pt_bac_1(a,b))