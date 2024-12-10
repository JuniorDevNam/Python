'''
Cho số nguyên n
 ở hệ thập phân (hệ cơ số 10). Hãy chuyển n 
 sang hệ nhị phân (hệ cơ số 2).
'''
n = int(input())
nhi_phan = bin(n).replace("0b", "")
print(nhi_phan)