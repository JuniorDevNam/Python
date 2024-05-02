N = int(input("Nhập số N: "))

def listprimes(N):
    prime_numbers = []
    for num in range(2, N + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)
    return prime_numbers

'''
Trong đoạn code trên, else không cùng hàng với if mà cùng hàng với for. 
Đây là một cấu trúc điều khiển đặc biệt trong Python được gọi là for-else.
Cấu trúc for-else cho phép chúng ta thực hiện một khối lệnh khi vòng lặp for kết thúc mà không gặp lệnh break. 
Trong trường hợp này, nếu số num không chia hết cho bất kỳ số nào từ 2 đến num - 1, 
thì vòng lặp sẽ kết thúc mà không gặp lệnh break, 
và khối lệnh trong else sẽ được thực hiện (tức là thêm số nguyên tố vào danh sách).
Nếu có lệnh break, tức là số num chia hết cho một số từ 2 đến num - 1, 
thì vòng lặp sẽ thoát ra và khối lệnh trong else sẽ không được thực hiện.
'''
#Hàm tự định nghĩa để xác định số nguyên tố
def isprime(N):
    if N<2:
        return str("Không phải số nguyên tố")
    uoc = 1
    dem = 2
    while dem < N//2:
        if N%dem == 0:
            uoc = uoc + 1
        dem = dem + 1
    if uoc == 1:
        return str("Là số nguyên tố")
    else:
        return str("Không phải số nguyên tố")
#Hàm tự định nghĩa để xác định số nguyên tố. Viết bởi Nam
def prime(N):
    if N<2:
        return "No"
    elif N == 2:
        return "Yes"
    elif N > 2:
        for x in range(2,N):
            if N%x == 0:
                return "No"
        else:
            return "Yes"
'''
Khi bạn thụt lề dòng else vào để ngang với if, nó sẽ chạy không đúng 
vì nó sẽ trở thành một phần của câu 
lệnh if bên trong vòng lặp for. Điều này có nghĩa là khi N chia hết cho x, 
hàm sẽ trả về "No", nhưng nếu không chia hết, hàm sẽ trả về "Yes" 
ngay lập tức mà không kiểm tra các giá trị x tiếp theo. Đ
iều này dẫn đến việc hàm trả về kết quả sai.

Trong khi đó, khi dòng else thụt lề để ngang với dòng for, 
nó sẽ được thực thi khi vòng lặp for kết thúc mà không có lệnh return 
nào được thực thi. Điều này có nghĩa là khi N không chia hết cho bất kỳ 
giá trị x nào trong phạm vi từ 2 đến N-1, hàm sẽ trả về "Yes", 
chỉ ra rằng N là một số nguyên tố. Đây là cách hoạt động đúng của hàm.


Có một số cách để tối ưu hàm kiểm tra số nguyên tố của bạn. 
Một cách đơn giản là thay đổi phạm vi của vòng lặp for từ range(2,N) 
thành range(2,int(N**0.5)+1). Điều này giúp giảm số lần lặp lại của 
vòng lặp và tăng tốc độ thực thi của hàm.

Ngoài ra, bạn cũng có thể thêm một câu lệnh if để kiểm tra xem 
N có chia hết cho 2 hay không. Nếu N chia hết cho 2 và N khác 2, 
thì N không phải là số nguyên tố và hàm sẽ trả về "No" ngay lập tức.
Sau đó, bạn có thể thay đổi phạm vi của vòng lặp for thành 
range(3,int(N**0.5)+1,2) để chỉ kiểm tra các số lẻ.

Đây là một phiên bản tối ưu hơn của hàm kiểm tra số nguyên tố:
'''

#Hàm được tối ưu. Bởi Bing.
def prime_toiuu(N):
    if N < 2:
        return "No"
    elif N == 2:
        return "Yes"
    elif N % 2 == 0:
        return "No"
    else:
        for x in range(3,int(N**0.5)+1,2):
            if N % x == 0:
                return "No"
        else:
            return "Yes"
'''
Vòng lặp for trong hàm kiểm tra số nguyên tố của bạn hoạt động 
bằng cách lặp qua một dãy các giá trị x từ 2 đến căn bậc hai của N 
(hoặc từ 3 đến căn bậc hai của N với bước nhảy là 2 nếu bạn sử dụng phiên bản tối ưu hơn của hàm).
Đối với mỗi giá trị x, hàm sẽ kiểm tra xem N có chia hết cho x hay không. 
Nếu N chia hết cho x, điều đó có nghĩa là N không phải là số nguyên tố và 
hàm sẽ trả về "No" ngay lập tức.

Nếu vòng lặp kết thúc mà không có lệnh return nào được thực thi,
 điều đó có nghĩa là N không chia hết cho bất kỳ giá trị x nào
 trong phạm vi từ 2 đến căn bậc hai của N. Khi đó, hàm sẽ trả về "Yes"
   để chỉ ra rằng N là một số nguyên tố.

Việc sử dụng phạm vi từ 2 đến căn bậc hai của N 
(hoặc từ 3 đến căn bậc hai của N với bước nhảy là 2) 
trong vòng lặp for giúp tăng tốc độ thực thi của hàm. 
Điều này là do nếu một số không phải là số nguyên tố, 
thì nó sẽ có ít nhất một ước số nhỏ hơn hoặc bằng căn bậc hai của nó.
'''


print("Đang sử dụng hàm theo SGK:",isprime(N))
print("Số nguyên tố? (Đang sử dụng hàm chưa tối ưu) -",prime(N))
print("Số nguyên tố? (Đang sử dụng hàm đã tối ưu) -",prime_toiuu(N))
print("Các số nguyên tố từ 1 đến N:",listprimes(N))
