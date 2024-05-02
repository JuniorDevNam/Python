# Nhập hai xâu s1 và s2 từ bàn phím
s1 = input("Nhập xâu s1: ")
s2 = input("Nhập xâu s2: ")

# Tính vị trí chèn là len(s2)//2
pos = len(s2)//2

# Chèn xâu s1 vào giữa s2 tại vị trí pos
s3 = s2[:pos] + s1 + s2[pos:]

# In kết quả ra màn hình
print("Xâu kết quả là:", s3)