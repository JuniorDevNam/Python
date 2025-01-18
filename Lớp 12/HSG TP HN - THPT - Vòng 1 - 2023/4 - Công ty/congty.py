import sys, os
input_file = os.path.join(sys.path[0],'ngiay.inp')
output_file = os.path.join(sys.path[0],'ngiay.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

