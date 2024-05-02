n = int(input("Nhập n: ")) # Nhập số n từ bàn phím
A = [0, 1] # Tạo một danh sách A gồm hai số đầu tiên của dãy Fibonacci
for i in range(2, n): # Lặp qua các chỉ số từ 2 đến n-1
    A.append(A[i-1] + A[i-2]) # Thêm vào A tổng của hai số hạng trước đó
print(A)