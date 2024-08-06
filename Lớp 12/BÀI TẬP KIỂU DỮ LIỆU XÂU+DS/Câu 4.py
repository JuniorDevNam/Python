# Cho hai xâu s1, s2. 
# Viết đoạn chương trình chèn xâu s1 vào giữa s2, tại vị trí len(s2)//2. 
# In kết quả ra màn hình.

#test:
# s1: day_la_xau_1
# s2: day_la_xau_2
#ket qua:
#tách s2: "day_la" "_xau_2"
#chèn s1: day_laday_la_xau_1_xau_2

s1 = str(input("Nhập xâu s1: "))
s2 = str(input("Nhật xâu s2: "))
s2_1 = s2[:len(s2)//2]
s2_2 = s2[len(s2)//2:]
r = s2_1 + s1 + s2_2
print(r)