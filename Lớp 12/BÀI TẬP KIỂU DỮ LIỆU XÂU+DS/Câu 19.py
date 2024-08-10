# Tìm chuỗi con xuất hiện nhiều nhất trong một chuỗi.

chuoi = str(input("Nhập chuỗi: "))
dem = {}
for s in chuoi.split():
    dem[s] = dem.get(s, 0) + 1
r = max(dem, key=dem.get)
print(r)