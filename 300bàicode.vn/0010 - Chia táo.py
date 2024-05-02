'''
Đề bài
Viết chương trình nhập vào số học sinh của 1 lớp (HS) và số táo trong rổ (T). 
Hãy chia đều số táo cho tất cả học sinh trong lớp, mỗi bạn sẽ được bao nhiêu quả táo?
Còn dư lại bao nhiêu quả?

Dữ liệu vào
Gồm 1 dòng có 2 số nguyên cách nhau bởi dấu cách theo thứ tự là T và HS

Dữ liệu ra
Là số táo mỗi học sinh được chia và tổng số táo còn dư, các số cách nhau bởi dấu cách

Ví dụ
Input #1 

28 11
Output #1 

2 6
'''
input = input()
T, HS = map(int, input.split())
chia = T//HS
du = T%HS
print(chia, du)