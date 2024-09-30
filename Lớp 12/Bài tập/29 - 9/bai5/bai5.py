S = 'abacbfc'
ds = {}
for x in sorted(S):
    if x in ds:
        ds[x] += 1
    else:
        ds[x] = 1
print(ds)
for key, value in ds.items():
    print(f'{key}: {value}')