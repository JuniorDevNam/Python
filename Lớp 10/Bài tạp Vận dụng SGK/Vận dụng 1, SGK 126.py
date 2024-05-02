s=input("Nhập hai số tự nhiên cách nhau 1 khoảng trống: ")
A=s.split(" ")
a=int(A[0])
b=int(A[1])
r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
print("ƯCLN của a và b là: ",b) 