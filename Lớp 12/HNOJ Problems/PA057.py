'''
Cho số nguyên dương a. 
Hãy vẽ hình chữ nhật kích thước 10 x a với các cạnh sử dụng dấu *.
Ví dụ, với a = 4 hình chữ nhật được vẽ như sau:

**********
*        *
*        *
**********

'''
a = int(input())
r = "**********"
d = "*        *"
print(r)
for x in range(1,a-1):
    print(d)
print(r)