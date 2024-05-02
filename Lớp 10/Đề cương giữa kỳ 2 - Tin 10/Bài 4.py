# Viết chương trình in ra các số tự nhiên liên tiếp sao cho tổng của
# chúng không vượt quá N, với N là 1 số nhập từ bàn phím.

# Nhập N:
N = int(input("Nhập 1 số nguyên N: "))

soTuNhien = [] #Tạo danh sách số TN rỗng
tongSTN = 0

for x in range(1,N):
    tongSTN = tongSTN + x #Tính tổng các STN lần lượt 
                            #Bằng vòng lặp
    if tongSTN < N: #Nếu tổng các số TN bé hơn N 
        soTuNhien.append(x) #TM đề bài và cho vào danh sách
    else: #Khi tổng các STN ko còn TM
        break #Kết thúc

#Xuất kết quả
print("Các số tự nhiên liên tiếp có tổng không vượt quá N là:",soTuNhien)
