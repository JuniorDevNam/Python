import os, sys
input_file = os.path.join(sys.path[0],"triseqlist.inp")
output_file = os.path.join(sys.path[0],"triseqlist.out")
sys.stdin = open(input_file,"r")
sys.stdout = open(output_file,"w")

n = int(input())
