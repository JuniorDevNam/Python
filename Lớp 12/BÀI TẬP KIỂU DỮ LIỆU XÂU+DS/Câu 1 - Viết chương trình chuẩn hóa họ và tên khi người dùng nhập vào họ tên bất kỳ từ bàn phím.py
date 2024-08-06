#Test: NGUyễn hỒnG nAM
#Ket qua: Nguyễn Hồng Nam
s = str(input("Họ và tên: "))
l = s.split(" ")
r = ""
for str in l:
    str = str.lower()
    r += str.capitalize() + " "
print(r)