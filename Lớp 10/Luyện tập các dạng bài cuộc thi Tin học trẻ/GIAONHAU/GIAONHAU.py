#Viết chương trình nhập vào bốn số thực trong đó . 
#Cho biết hai đoạn và trên trục số có điểm chung không?
# Input: Gồm bốn dòng, mỗi dòng chứa một số thực tương ứng với bốn số .
# Output: Ghi ra hoặc tương ứng với kết quả của bài toán là hai đoạn có hay không có điểm chung.

import sys
from os.path import join

input_file = join(sys.path[0], 'GIAONHAU.INP')
output_file = join(sys.path[0], 'GIAONHAU.OUT')
sys.stdin = open(input_file, 'r') # mở file để đọc
sys.stdout = open(output_file, 'w') # mở file để ghi

a = float(input())
b = float(input())
c = float(input())
d = float(input())
if b < c or d < a:
  print("YES")
else:
  print("NO")