import sys, os
input_file = os.path.join(sys.path[0],'ngiay.inp')
output_file = os.path.join(sys.path[0],'ngiay.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
n = int(input())
time = [0,':',0,':',0]
if n < 60:
    time[4] = str(n)
if 60 <= n < 3600:
    time[2] = str(n // 60)
    time[4] = str((n - int(time[2])*60))
if 3600 <= n < 86400:
    time[0] = str(n // 3600)
    t = (n - int(time[0])*3600)
    time[2] = str(t // 60)
    time[4] = str((t - int(time[2])*60))
for x in range(0,5,2):
    if len(time[x]) < 2:
        time[x] = '0' + time[x]
print(''.join(str(x) for x in time))