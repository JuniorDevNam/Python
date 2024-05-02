import random

count = int(input("Nhập số phần tử muốn có trong A: "))
A = []
viTri = []
def A_custom(count):
    for x in range(count):
        A.append(float(input("Nhập số thứ "+str(x+1)+": ")))
    return "Dãy số A là: "+str(A)

def A_random(count):
    for x in range(count):
        A.append(random.randrange(-999,999))
    return "Dãy số A là: "+str(A)

print("Chọn 1 trong 2 cách khởi tạo dãy số A: random (1) và tự nhập (2)")
cach = int(input("Chọn cách 1 hay 2?: "))
while cach != 1 and cach != 2:
    cach = int(input("Không hợp lệ, cách 1 hay cách 2?: "))

if cach == 1:
    print(A_random(count))
    for x in range(count):
        if A[x] == max(A):
            viTri = x
    print("Số lớn nhất của dãy số A là:",max(A),"ở vị trí",sorted(viTri))
if cach == 2:
    print(A_custom(count))
    for x in range(count):
        if A[x] == max(A):
            viTri.append(x)
    print("Số lớn nhất của dãy số A là:",max(A),"ở vị trí",sorted(viTri))