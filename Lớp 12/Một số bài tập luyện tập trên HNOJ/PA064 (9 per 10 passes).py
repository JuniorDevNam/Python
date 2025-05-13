import re

S = input()

# Biểu thức chính quy để kiểm tra tên file hợp lệ
pattern = r'^[a-zA-Z0-9_-]+\.(py|PY)$'

if re.match(pattern, S):
    print("YES")
else:
    print("NO")