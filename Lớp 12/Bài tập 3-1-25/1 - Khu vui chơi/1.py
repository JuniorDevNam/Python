import sys, os
input_file = os.path.join(sys.path[0],'khuvuichoi.inp')
output_file = os.path.join(sys.path[0],'khuvuichoi.out')
sys.stdin = open(input_file,'r')
sys.stdout = open(output_file, 'w')
gbd, gkt = map(int, input().split())
tgian = gkt - gbd
if tgian <= 4:
    if gkt <= 12:
        print(tgian * 6)
    elif gbd >= 12:
        print(tgian * 10)
else:
    if gkt <= 12:
        print((tgian-4)*3 + 4*6)
    elif gbd >= 12:
        print((tgian-4)*5 + 4*10)
    elif gbd <= 12 < gkt:
        tsang = 12 - gbd
        tchieu = gkt - 12
        if tsang <= 4:
            du = tchieu-(4-tsang)
            print(tsang*6 + (tchieu-du)*10 + du*5)
        else:
            du = tsang-4
            print(4*6 + du*3 + tchieu*5)
