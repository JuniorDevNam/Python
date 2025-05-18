S = input()
check_palindrome = True
for i in range(len(S) // 2): 
    if S[i] != S[-(i + 1)]:
        check_palindrome = False
        break
if check_palindrome:
    print("YES")
else:       
    print("NO")