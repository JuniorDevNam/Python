N = 5
A = '1  2  1  2  1'
ds = {}
for x in list(map(int,A.split())):
    if x in ds:
        ds[x] += 1
    else:
        ds[x] = 1
for key, value in my_dict.items():
    print(f'{key}: {value}')
