'''
Đề bài
Viết chương trình nhập vào 1 số nguyên dương n. In ra những số chia hết cho 3 trong các số từ 1 đến n, nếu không có số nào thì in -.

Dữ liệu vào
Một số nguyên dương n

Dữ liệu ra
Một dòng các số chia hết cho 3 từ 1 đến n, mỗi số cách nhau 1 dấu cách; nếu không có thì in -


Ví dụ
Input #1 
13
Output #1 
3 6 9 12

Input #2 
21
Output #2 
3 6 9 12 15 18 21

Nguồn
https://www.facebook.com/300baicode.vn/posts/117067554081651
'''
def find_multiples_of_3(n):
    # Bắt đầu từ số lớn nhất chia hết cho 3 nhỏ hơn hoặc bằng n
    start = n if n % 3 == 0 else n - n % 3
    # Tạo ra một list các số chia hết cho 3
    return " ".join(list(str(i) for i in range(3, start + 1, 3)))
n = int(input())
print(find_multiples_of_3(n))