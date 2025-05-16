import os, sys
input_file = os.path.join(sys.path[0], "hoicho.INP")
sys.stdin = open(input_file, 'r')
# số điểm bán n, số đường đi m, số lượng điểm bán đặc biệt k, số lượt chơi q
n, m, k, q = map(int, input().split())
sk = list(map(int, input().split()))
am = [list(map(int, input().split())) for _ in range(m)]
qxd = [list(map(int, input().split())) for _ in range(q)]


def sorted_openable_doors(d):
    A = []
    for arr in am:
        if arr[2] % d == 0:
            A.append(arr)
    return A


def find_next_nodes(start, arr):
    A = []
    for i in arr:
        if i[0] == start:
            A.append(i[1])
    return A


for i in range(q):
    x, d = qxd[i][0], qxd[i][1]
    if d == 1:
        print(1)
    else:
        count = 0
        minCount = 10**18
        destination = False
        while destination == False:
            visited = set()
            start = x
            visited.add(start)
            for arr in sorted_openable_doors(d):
                
        if count < minCount:
            minCount = count
        print(minCount)

