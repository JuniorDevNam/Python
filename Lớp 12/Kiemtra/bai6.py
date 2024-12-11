T = int(input("Số bộ dữ liệu cần kiểm tra T: "))
for t in range(T):
    N = int(input("Số phần tử của dãy N: "))
    A = list(map(int,input("Dãy số gồm N số nguyên cách nhau bởi khoảng trắng: ").split()))
    count = 0
    for i in range(1,N):
        for j in range(i+1,N):
            if i * A[i] > j * A[j]:
                count += 1
    print(count)