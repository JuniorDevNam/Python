'''
Cho danh sách a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n=10 phần tử. 
Lưu ý:
•	Phần tử đầu tiên trong danh sách là a[0]=2, phần tử thứ 2 là a[1]=4, …
•	Phần tử cuối cùng của danh sách là a[-1] = a[9]=8, phần tử kề cuối là a[-2] = a[8] = 6, …
Yêu cầu:
Bài 10: Viết chương trình Python tính số lượng các phần tử liên tiếp đan dấu nhiều nhất 
(dãy phần tử liên tiếp được gọi là đan dấu nếu tích hai phần tử liên tiếp âm).
'''
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
so_lg, temp = 0, 1
for i in range(len(a)-1):
    if a[i]*a[i+1] < 0:
        temp += 1
    else:
        if temp > so_lg:
            so_lg -= so_lg
            so_lg += temp
        temp -= (temp-1)
print("Số phần tử liên tiếp đan dấu là {}".format(so_lg))