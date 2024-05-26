'''
Đề bài
Viết chương trình nhập vào tổng số giây là một số nguyên, in ra giờ:phút:giây.

Dữ liệu vào
Một số nguyên là tổng số giây

Dữ liệu ra
Kết quả đổi được theo dạng giờ:phút:giây

Ví dụ
Input #1 

4010
Output #1 

1:6:50
'''
input = int(input())
h = input // 3600 #chia lấy nguyên
m = (input % 3600) // 60 
s = (input % 3600) % 60 #chia lấy dư
print(f'{h}:{m}:{s}')