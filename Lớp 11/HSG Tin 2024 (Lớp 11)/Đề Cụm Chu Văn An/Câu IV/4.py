'''
Để giải quyết bài toán này, chúng ta có thể sử dụng một thuật toán tham lam (greedy algorithm). Ý tưởng là chọn các phần tử lớn nhất trong dãy sao cho tổng của 3 phần tử bất kỳ không vượt quá tổng của các phần tử còn lại.

Dưới đây là cách thực hiện:

1. Sắp xếp dãy số theo thứ tự giảm dần: Điều này giúp chúng ta có thể chọn các phần tử lớn nhất trước.
2. Chọn các phần tử lớn nhất: Bắt đầu từ phần tử lớn nhất, chọn nó vào danh sách các phần tử đã chọn. Nếu tổng của 3 phần tử đã chọn vượt quá tổng của các phần tử còn lại, loại bỏ phần tử này.
3. Lặp lại bước 2 cho các phần tử còn lại: Tiếp tục chọn các phần tử lớn nhất khác cho đến khi không thể chọn thêm phần tử nào.
'''
from sys import path as dir
from os.path import join
inp = join(dir[0],"CPT.INP")
out = join(dir[0],"CPT.OUT")

def cpt(A):
    # Sắp xếp dãy số theo thứ tự giảm dần
    A.sort(reverse=True)
    # Danh sách các phần tử đã chọn
    selected_elements = []
    draft = []
    # Tổng của các phần tử còn lại
    remaining_sum = sum(A)
    print("o:",remaining_sum)
    for a in A:
        # Thêm phần tử vào danh sách đã chọn
        draft.append(a)
        # Giảm tổng của các phần tử còn lại
        remaining_sum -= a
        print("-a:",remaining_sum)
        # Kiểm tra xem tổng của 3 phần tử đã chọn có vượt quá tổng của các phần tử còn lại không
        if sum(draft) > remaining_sum:
            # Nếu có, loại bỏ phần tử vừa thêm vào
            draft.pop()
        else:
            selected_elements.append()
    # In ra số lượng các phần tử đã chọn
    #print(len(selected_elements))
    return len(selected_elements)


def solve(A):
    # Sắp xếp dãy số theo thứ tự giảm dần
    A.sort(reverse=True)
    
    # Danh sách các phần tử đã chọn
    selected_elements = []
    
    # Tổng của các phần tử còn lại
    remaining_sum = sum(A)
    print("o:",remaining_sum)
    for a in A:
        print("a:",a)
        # Thêm phần tử vào danh sách đã chọn
        selected_elements.append(a)
        
        # Giảm tổng của các phần tử còn lại
        remaining_sum -= a
        print("o-a:",remaining_sum)
        # Kiểm tra xem tổng của 3 phần tử đã chọn có vượt quá tổng của các phần tử còn lại không
        if sum(selected_elements) > remaining_sum:
            # Nếu có, loại bỏ phần tử vừa thêm vào
            selected_elements.pop()
            break
    
    # In ra số lượng các phần tử đã chọn
    print(len(selected_elements))
    return len(selected_elements)


# Đọc dữ liệu từ file CPT.INP
with open(inp, "r") as i:
    s = i.readlines()
n = int(s[0])
A = list(map(int, s[1].split()))
print(n,A)
# Gọi hàm giải quyết bài toán
result = solve(A)
r = cpt(A)
# Ghi kết quả ra file CPT.OUT
with open(out, "w") as o:
    o.write(str(result))