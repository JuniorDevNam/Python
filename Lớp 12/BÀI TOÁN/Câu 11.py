'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 11: Viết chương trình Python tính số lượng các phần tử không tăng nhiều nhất.
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
s, tmp = 1, 1
for i in range(len(a)-1):
    if a[i+1] < a[i]:
        tmp += 1
    else:
        if tmp > s:
            s = tmp
        tmp -= (tmp-1)
print(s)