#integer = int(input("Nhập 1 số nguyên: "))
#floatnum = float(input("Nhập 1 số thực: "))
#string = str("Nhập 1 chuỗi: ")
characters = input("Nhập 1 thứ bất kỳ: ")
thg = []
hoa = []
h, t = 0, 0
for i in range(len(characters)):
    if characters[i].isupper():
        h = h + 1
        hoa.append(characters[i])
    elif characters[i].islower():
        t = t + 1
        thg.append(characters[i])
print(h)
print(t)
thg = "".join(thg)
hoa = "".join(hoa)
print(thg)
print(hoa)

