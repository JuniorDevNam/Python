S = str(input('S: '))
t, ds = '', []
def chuoi(S):
    return S[1:] + S[0]
for i in range(len(S)):
    ds.append(chuoi(S))
    S = chuoi(S)
print(ds)