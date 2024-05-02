'''
Đề bài
Nhập một số tiền N (N<=1.000.000) đồng (N là số chia hêt cho 1.000), 
đổi ra xem được bao nhiêu tờ 5.000 đồng, bao nhiêu tờ 2.000 đồng, 
bao nhiêu tờ 1.000 đồng sao cho tổng số tờ là ít nhất. 
Ví dụ N= 43.000 đ = 8 tờ 5.000 đ + 1 tờ 2.000 đ + 1 tờ 1.000 đ.

Dữ liệu vào
Một số nguyên n là số tiền cần đổi

Dữ liệu ra
Một dòng gồm 3 số theo thứ tự là số tờ 5.000, số tờ 2.000 và số tờ 1.000 cách nhau 1 dấu cách.

Ví dụ
Input #1 

42000
Output #1 

8 1 0
Input #2 

32000
Output #2 

6 1 0
'''
input = int(input())
nam = input//5000
hai = (input - nam*5000)//2000
mot = (input - (nam*5000 + hai*2000))//1000
print(nam, hai, mot)