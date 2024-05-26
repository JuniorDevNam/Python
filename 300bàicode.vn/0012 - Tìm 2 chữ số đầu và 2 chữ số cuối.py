'''Đề bài
Cho một số nguyên có 3 chữ số. In ra 2 chữ số cuối và 2 chữ số đầu của số vừa nhập

Dữ liệu vào
Một số nguyên n có 3 chữ số

Dữ liệu ra
Là 2 chữ số đầu và 2 chữ số cuối của n, cách nhau bởi dấu cách (nếu 2 chữ số là 0 thì in 00, nếu 2 chữ số mà có 0 phía trước thì vẫn in, vd 05)

Ví dụ
Input #1 
673
Output #1 
67 73
Input #2 
602
Output #2 
60 02
'''
n = input()
print(f'{str(n)[0]}{str(n)[1]} {str(n)[-2]}{str(n)[-1]}')