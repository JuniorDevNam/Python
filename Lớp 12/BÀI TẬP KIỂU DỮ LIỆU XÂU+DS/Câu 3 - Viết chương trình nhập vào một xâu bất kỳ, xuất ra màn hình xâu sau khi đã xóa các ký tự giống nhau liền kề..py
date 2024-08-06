#test: sssssiiiiiuuuuuuuuu
#ket qua: siu
inp = str(input('Nhập một xâu bất kỳ: '))
r = ""
for i in range(len(inp)):
    if i == len(inp) - 1 or inp[i] != inp[i+1]:
        r += inp[i]
print(r)