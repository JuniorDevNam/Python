from collections import defaultdict

# Nhập dữ liệu
p = list(map(str, input().split()))
d = str(input())

# Danh sách t9
t9 = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
phim = defaultdict(str)
t9_new = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

#Gán phím
for i in range(9):
    t9_new[i] = t9[int(p[i])-1]

for i in range(9):
    if t9_new[i] != '':
        for j in range(len(t9_new[i])):
            phim[t9_new[i][j]] = str(i+1) * (j+1)
#print(t9_new, phim)
# Tạo chuỗi kết quả
kq = phim[d[0]]
for s in d[1:]:
    if kq[-1] in phim[s]:
        kq += '#'
    if s == ' ':
        kq += '0'
    kq += phim[s]

#print(phim)
print(kq)

# Test
# Input:
# 4 6 2 5 1 7 9 3 8
# nhin sang trai vi em khong phai cua anh
# Expected result:
# 2211#111220666632210966631110999111088204411222#221061131110333993032211

#2211#11122 0 66663221 0 96663111 0 999111 0 882 0 4411222#221 0 6113111 0 333993 0 32211