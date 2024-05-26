'''
Đề bài
Viết chương trình nhập vào điểm Toán, Văn, Anh văn của 1 học sinh là các số thực. Tính trung bình của học sinh đó, biết rằng điểm Toán, Văn là hệ số 2.


Dữ liệu vào
Gồm 1 dòng có 3 số thực cách nhau bởi dấu cách theo thứ tự là Toan, Van và AnhVan.

Dữ liệu ra
Là điểm trung bình làm tròn đến 1 chữ số thập phân


Ví dụ
Input #1 
6 8 9
Output #1 
7.4
Input #2 
3 4 5
Output #2 
3.8'''

Toan, Van, AnhVan = map(float,input().split())
TB = (Toan*2 + Van*2 + AnhVan)/5
print(f'{TB:.1f}')