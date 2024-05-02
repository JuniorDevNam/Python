# Nhập vào 1 số nguyên N, viết chương trình in ra các số chẵn 
# từ 1 đến N và tính tổng các số đó.

#Nhập N:
N = int(input("Nhập 1 số nguyên N: "))
tong = 0 
soChan = []
# Dùng vòng lặp for để xét các số từ 1 đến N
for x in range(1,N+1):
    if x%2 == 0:
        soChan.append(x)
        tong = tong + x 

#Xuất kết quả:
print("Các số chẵn từ 1 đến N gồm:",soChan)
print("Tổng của các số đó là:",tong)

         
