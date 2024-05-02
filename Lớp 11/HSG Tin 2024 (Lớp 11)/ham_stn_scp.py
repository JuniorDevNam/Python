import time

#Số nguyên tố là số tự nhiên lớn hơn 1 không phải là tích của hai số tự nhiên nhỏ hơn. 
#Nói cách khác, số nguyên tố là những số chỉ có đúng hai ước số là 1 và chính nó.

#Ý tưởng: Dùng vòng lặp kiểm tra xem có tồn tại số mà n chia hết
#Nếu có nhiều hơn 1 (tức là n không chỉ chia hết cho n mà còn nhiều số khác), trả về 0
#1 là ngoại lệ
def kt_nt(n):
  print("Kiểm tra số nguyên tố:")
  d = 0
  if n <= 1:
    return 0
  else:
    for i in range(2, int(n**0.5) + 1):
      if n%i == 0:
        d+=1
      if d == 2:
        break
    if d == 0:
      return 1
    return 0
#Số chính phương là số tự nhiên có căn bậc hai là một số tự nhiên, 
#hay nói cách khác, số chính phương bằng bình phương của một số nguyên.

#Ý tưởng 1: Dùng vòng lặp để xem n có tồn tại số nguyên mà bình phương lên thì bằng n 
def kt_cp(n):
  print("Kiểm tra số chính phương")
  d=0
  for i in range(1,int(n**0.5)+1):
    if i*i == n:
      d += 1
  if d != 0:
    return 1
#Ý tưởng 2: Kiểm tra xem nếu căn bậc 2 của n bằng dạng số nguyên của căn bậc 2 của n (Tối ưu hơn)
def kt_cp_2(n):
  print("Kiểm tra số chính phương nhưng được tối ưu")
  if n**0.5 == int(n**0.5):
    return 1

#Test
a = [144, 276, 332, 425, 598, 701, 823, 999, 1005, 1024,93689387754, 5362325, 4256873, 6666666,3562345265]
b, c, d = [], [], []
for i in a:
  if kt_nt(i):
    b.append(i)
  if kt_cp(i):
    c.append(i)
  if kt_cp_2(i):
    d.append(i)
print("Dãy số nt:",b)
print("Dãy số cp:",c)
print("Dãy số cp tối ưu:",d)