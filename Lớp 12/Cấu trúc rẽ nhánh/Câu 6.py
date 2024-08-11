# Bài 6: Viết chương trình giải phương trình bậc 2: ax^2 + bx+c = 0 (a khác 0)
a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))

def pt_bac_2(a,b,c):
    if a == 0:
        return "Hệ số a không nằm trong yêu cầu đề bài"
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b+delta**0.5)/2*a
        x2 = (-b-delta**0.5)/2*a
        return "Phương trình có hai nghiệm phân biệt x1 = {}, x2 = {}".format(x1,x2)
    elif delta == 0:
        x2 = -b/2*a
        return "Phương trình có nghiệm kép x1 = x2 = {}".format(x2)
    elif delta < 0:
        return "Phương trình vô nghiệm"
    
print(pt_bac_2(a,b,c))