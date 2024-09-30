n = int(input('n: '))
t, m = 0, float('inf')
if n % 5 != 0 and n % 3 != 0:
    print('-1')
else:
    tui_nam = n // 5
    for i in range(tui_nam):
        kg_con_lai = n - (i*5)
        if kg_con_lai % 3 == 0:
            t = i + kg_con_lai // 3
            if t < m:
                m = t
    print(m)
