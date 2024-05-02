a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
n=10

#1. Tong cac phan tu danh sach
def cau1(a):
    return sum(a)
#2. dem so luong cac so hang duong va tong cac so hang duong
def cau2(a):
    count = 0
    tong = 0
    for x in a:
        if x > 0:
            count += 1
            tong = tong + x
    return count, tong
#3. trung binh cong ca danh sach, trung binh cong cua cac so duong trong danh sach
def tbc(ds):
    return sum(ds)/len(ds)
def cau3(a):
    duong = [x for x in a if x > 0]
    return tbc(a),tbc(duong)
#4. tim vi tri phan tu am dau tien trong danh sach
def cau4(a):
    for x in range(n):
        if a[x] < 0:
            r = x+1
            break
    return r
#5. tim vi tri cua phan tu duong cuoi cung trong danh sach
def cau5(a):
    for i in range(1,n+1):
        if a[-i] > 0:
            r = n - i + 1
            break
    return r
#6. tim phan tu lon nhat cua danh sach va vi tri phan tu lon nhat cuoi cung
def cau6(a):
    l = max(a)
    for x in range(n):
        if a[x] == l:
            r = x + 1
    return l, r
#7. tim phan tu lon thu nhi va vi tri cua cac phan tu do
def cau7(a):
    ds = sorted(a, reverse=True)
    nhi = ds[1]
    vt = []
    for x in range(n):
        if a[x] == nhi:
            vt.append(x+1)
    return nhi, vt
#8. tinh so luong cac so duong lien tiep nhieu nhat
def cau8(a):
    count = 0
    r = 0
    for x in a:
        if x > 0:
            count += 1
        else:
            count = count - count
        if count > r:
            r = count
    return r
#9. tinh so luong so duong lien tiep co tong lon nhat

#10. tinh so luong lien tiep 2 phan tu lien nhau co tich am nhieu nhat
def cau10(a):
    count = 0
    r = 0
    for x in range(n-1):
        if a[x]*a[x+1] < 0:
            count += 1
        else:
            count = count - count
        if count > r:
            r = count
    return r
#14. dem so luong cac phan tu bang voi gia tri X nhap tu ban phim
X = int(input('X: '))
def cau14(a, X):
    count = 0
    for i in range(n):
        if a[i] == X:
            count += 1
    return count
#15. chuyen cac phan tu duong len dau danh sach va in danh sach ra man hinh
def cau15(a):
    return sorted(a, reverse=True)

#16. tim so phan tu la duong va la so nguyen to, tim vi tri cua no trong danh sach
def snt(n):
  d = 0
  if n <= 1:
    return 0
  else:
    for i in range(2, int(n**0.5) + 1):
      if n%i == 0:
        return 0
    if d == 0:
      return 1
    return 0
def cau16(a):
    d = [x for x in a if x > 0]
    nt = [y for y in d if snt(y)]
    vt = []
    for i in range(n):
        for o in range(len(nt)):
            if a[i] == nt[o]:
                vt.append(i+1)
    return nt,vt
#17. chen 1 so m nhap tu ban phim vao dau danh sach, cuoi danh sach va vi tri thu 5 cua danh sach
m = int(input('m: '))
def cau17(a,m):
    dau = a.copy()
    cuoi = a.copy()
    thu5 = a.copy()
    cuoi.append(m)
    dau.insert(0,m)
    thu5.insert(4,m)
    return dau,cuoi,thu5
#18. chen danh sach [1,2,3] vao dau, cuoi va vi tri thu 5 cua danh sach
def cau18(a):
    ds = [1, 2, 3]
    return cau17(a,ds)
#19. xoa phan tu thu k nhap tu ban phim trong danh sach
k = int(input('k: '))
def cau19(a,k):
    xoa = a.copy()
    xoa.pop(k)
    return xoa
print("file by Nguyen Hong Nam")
print('a:',a)
print('1.',cau1(a))
print('2.',cau2(a))
print('3.',cau3(a))
print('4.',cau4(a))
print('5.',cau5(a))
print('6.',cau6(a))
print('7.',cau7(a))
print('8.',cau8(a))

print('10.',cau10(a))

print('14.',cau14(a, X))
print('15.',cau15(a))
print('16.',cau16(a))
print('17.',cau17(a,m))
print('18.',cau18(a))
print('19.',cau19(a,k))