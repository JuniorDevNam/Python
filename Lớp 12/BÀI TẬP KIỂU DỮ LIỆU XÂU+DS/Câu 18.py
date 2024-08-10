# Tìm chuỗi con dài nhất trong một chuỗi

chuoi = str(input("Nhập một chuỗi: ")).split()
tu_dai_nhat = max(chuoi, key=len)
print(tu_dai_nhat)
