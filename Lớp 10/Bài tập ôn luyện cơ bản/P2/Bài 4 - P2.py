'''Nhập vào hai số m, n, xuất ra dãy số bội 3 từ m đến n.'''

m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
while m > n:
    print("m lớn hơn n, không thỏa mãn đề bài")
    m = int(input("Nhập số m: "))
    n = int(input("Nhập số n: "))
S=[]
for k in range(m,n+1):
    if k%3==0:
        S.append(k)
print(S,end = " ")