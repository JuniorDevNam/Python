#test: Nammmm2307siuuu2007
#ket qua: Nammmmsiuuu
chuoi = str(input("Nhập vào một xâu bất kỳ gồm ký tự và số: "))
r = ""
for char in chuoi:
    if not char.isdigit():
        r += char
print(r)

