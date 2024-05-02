ss = float(input("Nhập số giây: "))

n = ss/86400
h = (n - int(n))*24
p = (h - int(h))*60
s = (p - int(p))*60
print(f"{int(n)}:{int(h)}:{int(p)}:{int(s)}")