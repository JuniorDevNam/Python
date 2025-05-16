import os, sys
from collections import deque

input_file = os.path.join(sys.path[0], "hoicho.INP")
sys.stdin = open(input_file, 'r')
n, m, k, q = map(int, input().split())
sk = set(map(int, input().split()))
am = [list(map(int, input().split())) for _ in range(m)]
qxd = [list(map(int, input().split())) for _ in range(q)]

def build_graph(d):
    graph = {}
    for u, v, w in am:
        if w % d == 0:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
    return graph

def bfs(x, d):
    graph = build_graph(d)
    visited = set()
    queue = deque()
    queue.append((x, 0))
    visited.add(x)
    while queue:
        u, steps = queue.popleft()
        if u in sk:
            return steps + 1
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append((v, steps + 1))
    return -1

for i in range(q):
    x, d = qxd[i][0], qxd[i][1]
    if d == 1:
        print(1)
    else:
        res = bfs(x, d)
        print(res if res != -1 else -1)