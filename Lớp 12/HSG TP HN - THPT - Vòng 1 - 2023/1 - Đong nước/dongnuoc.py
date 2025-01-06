import sys, os
input_file = os.path.join(sys.path[0],'dongnuoc.inp')
output_file = os.path.join(sys.path[0],'dongnuoc.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

import time
start_time = time.time()

n = int(input())
cnt = 0
if n > 5:
    namw = n // 5
    cnt += namw
    du = n % 5
    if n % 2 != 0:
        while du != 0:
            while du % 3 != 0:
                du += 5
                cnt -= 1
            ba = du / 3
            cnt += ba
        print(cnt)
    else:
        while du != 0:
            while du % 2 != 0:
                du += 5
                cnt -= 1
            ba = du // 3
            cnt += ba
            du %= 3
            while du < 2:
                du += 3
                cnt -= 1
            hai = du / 2
            cnt += hai
            du %= 2
        print(cnt)
elif n == 5 or n == 2 or n == 3: print(1)
elif n == 4: print(2)
else: print(-1)
end_time = time.time()
print(f"{end_time - start_time} giây")


