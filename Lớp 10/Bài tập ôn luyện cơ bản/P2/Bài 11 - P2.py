'''xuất các số nguyên tố từ n đến m.'''
n = int(input("nhập số n:"))
m = int(input("nhập số m:"))
snt = []
while m < n:
    print("m bé hơn n, không thỏa mãn đề bài")
    n = int(input("nhập số n:"))
    m = int(input("nhập số m:"))
for k in range (n,m+1):
    for x in range(2,k):
        if k%x==0:
            break
    else:
        snt.append(k)
print("Số nguyên tố từ khoảng",n,"đến",m,"là:",snt)
       
