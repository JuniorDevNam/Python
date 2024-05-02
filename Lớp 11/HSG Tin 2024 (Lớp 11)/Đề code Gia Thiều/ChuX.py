'''
Ý tưởng:
Có hai vòng lặp trong khoảng n là số ta cho vào từ file biểu thị cho tọa độ x và y
    0   1   2   3   4 
0   00  01  02  03  04

1   10  11  12  13  14

2   20  21  22  23  24  

3   30  31  32  33  34  

4   40  41  42  43  44
Xét hàng chéo đầu tiên từ trái qua phải ta có các tọa độ là 2 vòng lặp có số trùng nhau
In các số ở những vị trí đó
Tương tự với hàng chéo từ phải qua trái là các tọa độ có tổng bằng n-1
 '''

import sys
from os.path import join
filein = join(sys.join[0],"input.inp")
fileout = join(sys.join[0],"output.out")
with open(filein, 'r') as i:
    n = int(i.readlines())
for y in range(n):
    for x in range(n):
        if y==x or y+x == n-1:
            print(n-y, end=" ")
        else:
            print(" ",end=" ")
    print()