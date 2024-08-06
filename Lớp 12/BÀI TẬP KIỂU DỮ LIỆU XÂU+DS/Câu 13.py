#

ds = list(map(int, input('Nhap day so nguyen cach nhau boi dau cach: ').split()))
def kt_nt(n):
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
snt = [x for x in ds if kt_nt(x)]
print(snt)

#test: 1 3 2 5 4 98 45 23 56 7 8 10 9
#ket qua: 3 2 5 23 7
