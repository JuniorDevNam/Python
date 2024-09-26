x = str(input('x: '))
y = str(input('y: '))
n = int(input('n: '))
ds, chuoi = [x, y], ''
for i in range(2,n):
    chuoi = ds[i-1] + ds[i-2]
    print(chuoi)
    ds.append(chuoi)
print(max(ds))