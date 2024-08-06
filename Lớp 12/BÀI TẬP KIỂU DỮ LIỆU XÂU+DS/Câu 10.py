# Viết chương trình dung phương pháp list comprehension để tạo các list sau:
#a) Dãy các số là bội của 3 và nhỏ hơn 100
#b) Dãy 10 số chính phương đầu tiên

a = [x for x in range(3,100,3)]
b = [x**2 for x in range(1,11)]
print(a)
print(b)