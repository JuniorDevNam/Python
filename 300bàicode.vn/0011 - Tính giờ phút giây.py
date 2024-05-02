'''
Đề bài
Viết chương trình nhập vào tổng số giây là một số nguyên, in ra giờ:phút:giây.

Dữ liệu vào
Một số nguyên là tổng số giây

Dữ liệu ra
Kết quả đổi được theo dạnggiờ:phút:giây

Ví dụ
Input #1 

4010
Output #1 

1:6:50
'''
input = int(input())
h = input/3600
p = (h - int(h)) * 60
s = (p - int(p)) * 60 
print(f"{int(h)}:{int(p)}:{int(s)}")