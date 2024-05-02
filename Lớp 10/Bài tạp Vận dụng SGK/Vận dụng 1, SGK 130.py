# Gỉai thích ý nghĩa của những lệnh return
def prime(n): #Hàm prime (số nguyên tố) với tham số n
    if n < 2: #Nếu n bé hơn 2
        return False #Trả về Sai (False)
    C = 0 
    k = 2
    while k < n: #Khi k bé hơn n
        if n%k == 0: #Nếu n chia cho k dư 0 (n chia hết cho k)
            return False #Trả về Sai (False)
        k = k+1
    return True #Những trường hợp còn lại của n mà không hợp với điều kiện bên trên
                #Sẽ được trả về tại đây là Đúng (True)