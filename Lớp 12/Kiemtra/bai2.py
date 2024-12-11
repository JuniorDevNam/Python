B = int(input("Nhập Số bộ dữ liệu cần kiểm tra B: "))
for x in range(B):
    N, K = map(int,input("Nhập N, K cùng 1 dòng cách nhau bởi khoảng trắng: ").split())
    A = list(map(str,input("Nhập dãy số cách nhau bởi khoảng trắng: ").split()))
    if len(A) > N:
        print("Lỗi, dãy số có số phần tử lớn hơn N")
    else:
        count = 0
        for x in A:
            for y in x:
                if y == str(K):
                    count += 1
        print(count)

