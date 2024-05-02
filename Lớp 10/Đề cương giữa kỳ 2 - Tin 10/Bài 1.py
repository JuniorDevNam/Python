#Viết chương trình nhập vào một số nguyên N từ bàn phím, 
#kiểm tra và in ra thông báo số đó có phải là số chẵn chia hết cho 7 hay không?

#Nhập N
N = int(input("Nhập 1 số nguyên N: "))
print("Số N vừa nhập là:",N)

if N%2 == 0 and N%7 == 0:
    print("N (",N,") là số chẵn chia hết cho 7")
else:
    print("N (",N,") không là số chẵn chia hết cho 7")