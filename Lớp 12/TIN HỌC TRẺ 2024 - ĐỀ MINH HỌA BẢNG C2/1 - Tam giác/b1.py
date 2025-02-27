T = int(input())
n = [int(input()) for _ in range(T)]

#Tạo tất cả các tập hợp tam giác, vì T tối đa = 10 nên sẽ chỉ có tối đa 120 tam giác được tạo ra
def snt(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

for x in n:
    triangle = []
    for i in range(1,x-1):
        for j in range(i+1,x):
            for k in range(j+1,x+1):
                triangle.append([i,j,k])
    #print(triangle)
    count = 0
    for y in triangle:
        x_snt = 0
        v_ksnt = 0
        c1 = y[0] + y[1]
        c2 = y[0] + y[2]
        c3 = y[1] + y[2]
        if snt(c1): 
            x_snt += 1 
        else: 
            v_ksnt += 1
        if snt(c2): 
            x_snt += 1
        else: 
            v_ksnt += 1
        if snt(c3): 
            x_snt += 1
        else: 
            v_ksnt += 1
        #print(c1,c2,c3)
        #print(snt(c1),snt(c2),snt(c3))
        #print(x_snt,v_ksnt)
        if x_snt == 3 or v_ksnt == 3:
            count += 1
            #print(count)
    #print("----")
    print(count)