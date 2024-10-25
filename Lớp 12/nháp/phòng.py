p = 50
t = 400000
dsp = p*t
while p > 0:
    if p*t >= dsp:
        dsp = (p*t)
        kq = t
    p -= 1
    t += 10000
print(kq)