import time
start_time = time.time()

import sys, os
input_file = os.path.join(sys.path[0],'dongnuoc.inp')
output_file = os.path.join(sys.path[0],'dongnuoc.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
def min_steps(n):
    if n in [2, 3, 5]:
        return 1
    if n == 4:
        return 2
    cnt = 0
    trigger = False
    while n > 0:
        if n % 5 == 0:
            cnt += n // 5
            break
        elif n >= 5 and trigger == False:
            cnt += n // 5
            n %= 5
        elif n % 3 == 0:
            cnt += n // 3
            break
        elif n % 2 == 0:
            cnt += n // 2
            break
        elif n < 2:
            n += 5
            cnt -= 1
            trigger = True
    return cnt

n = int(input())
print(min_steps(n))

end_time = time.time()
print(f"{end_time - start_time} giây")