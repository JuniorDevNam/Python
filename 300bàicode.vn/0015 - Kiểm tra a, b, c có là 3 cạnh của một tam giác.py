'''
Đề bài
Viết chương trình kiểm tra xem 3 số a, b, c nhập từ bàn phím có là 3 cạnh của một tam giác hay ko? Nếu phải thì tính chu vi và diện tích của tam giác đó, ngược lại thông báo 3 số đó ko phải là 3 cạnh của tam giác

Dữ liệu vào
Một dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c.

Dữ liệu ra
Dòng 1: “Day khong phai la 3 canh cua mot tam giac” hoặc “Day la 3 canh cua mot tam giac”, nếu là trường hợp 2 thì thêm dòng 2 là chu vi và diện tích nằm trên cùng một dòng, cách nhau bởi dấu cách, chu vi làm tròn đến 2 chữ số thập phân, diện tích làm tròn đến 1 chữ số thập phân.

Ví dụ
Input #1 
1 2 3
Output #1 
Day khong phai la 3 canh cua mot tam giac

Input #2 
3 4 5
Output #2 
Day la 3 canh cua mot tam giac
12.00 6.0
'''
a, b, c = map(int,input().split())
if a + b > c and a + c > b and b + c > a:
    cv = a + b + c
    p = cv/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print("Day la 3 canh cua mot tam giac")
    print(f'{cv:.2f} {s:.1f}')
else:
    print("Day khong phai la 3 canh cua mot tam giac")