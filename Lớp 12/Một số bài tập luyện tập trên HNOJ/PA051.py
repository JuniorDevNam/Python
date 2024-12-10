'''
Cho số nguyên dương n. 
Kiểm tra xem n có phải là số đối xứng hay không.

Các số đối xứng là các số không thay đổi khi viết theo thứ tự từ trái sang phải
 hoặc từ phải sang trái.

https://hnoj.edu.vn/problem/pa051
'''
n = int(input())
n1 = str(n)
n2 = ""
#cách 1
for x in range(1,len(n1)+1):
    n2 = n2 + n1[-x]
#cách 2:
n2 = n1[::-1]
if n1 == n2:
    print("YES")
else:
    print("NO")