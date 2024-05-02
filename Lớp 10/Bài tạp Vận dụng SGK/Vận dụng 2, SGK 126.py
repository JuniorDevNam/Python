n = int(input("Nhập số tự nhiên n: "))
ds_hs = []
ds_hs.append(str(input("Nhập họ tên học sinh thứ "+str(i+1)+": ")) for x in range(n))
t = 0
s=input("Nhập một tên: ")
for i in range(0,n):
    ten=ds_hs[i].split()
    if s == ten[len(ten)-1]:
        t = t+1
print("Vậy trong lớp có số bạn cùng tên đó là: ",t)   

