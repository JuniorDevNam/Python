import sys, os

input_file = os.path.join(sys.path[0],"xau.INP")
output_file = os.path.join(sys.path[0],"xau.OUT")
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

def is_palindrome(s: str) -> bool:
    i = 0
    length = len(s)
    result = True
    while i < length // 2 and result:
        i += 1
        result = s[i - 1] == s[length - i]
    return result

ans = 0
s = str(input())
tmp = ''
for i in range(len(s)):
    tmp += s[i]

    if len(tmp) >= 2 and is_palindrome(tmp):
        ans += 1
    for j in range(i + 1, len(s)):
        tmp += s[j]
        if len(tmp) >= 2 and is_palindrome(tmp):
            ans += 1
    tmp = ''
print(ans)