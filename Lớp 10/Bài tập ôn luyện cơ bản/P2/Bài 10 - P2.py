'''Giải hai bài toán cổ: 
100 trâu 100 bó cỏ và vừa gà vừa chó 36 con 100 chân'''

'''Bài toán 100 trâu 100 bó cỏ là một bài toán 
về hệ phương trình tuyến tính.
 Bài toán cho biết có ba loại trâu A, B và C,
mỗi loại trâu ăn một lượng bó cỏ khác nhau: 
A ăn 5 bó, B ăn 3 bó và C ăn 1 bó. 
Bài toán yêu cầu tìm số lượng của mỗi loại trâu nếu 
biết tổng số trâu là 100 và tổng số bó cỏ là 100'''
#Ta gọi trâu 1 là a, trâu 2 là b, trâu 3 là c
#có 5a + 3b + c = 100 (bó cỏ)
#và a + b + c = 100 (trâu)

def bing_chat_lam():
    # Tạo ma trận hệ số của các ẩn
    A = [[1, 1, 1], [5, 3, 1]]

    # Tạo vector hằng số
    b = [100, 100]

    # Khử Gauss để biến đổi ma trận A thành ma trận tam giác trên
    n = len(A)
    for i in range(n):
        # Tìm phần tử chính khác 0
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    # Hoán vị hai hàng i và j
                    A[i], A[j] = A[j], A[i]
                    b[i], b[j] = b[j], b[i]
                    break
        # Khử các phần tử dưới hàng i
        for j in range(i + 1, n):
            # Tính hệ số khử
            factor = A[j][i] / A[i][i]
            # Trừ hàng i lần lượt cho các hàng dưới
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Thế ngược để tìm nghiệm
    x = [0] * n
    for i in range(n - 1, -1, -1):
        # Tính tổng các hệ số nhân với nghiệm đã biết
        s = sum(A[i][j] * x[j] for j in range(i + 1, n))
        # Tính nghiệm của ẩn hiện tại
        x[i] = (b[i] - s) / A[i][i]
    # In ra nghiệm
    #print(x)
    return x

