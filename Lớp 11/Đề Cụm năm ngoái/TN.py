#Trắc nghiệm:
'''
1.C
2. Lỗi sai cú pháp: 'printt' sửa lại: 'print'
3. B
4. True
5. True
6. False
7. True
8. False


11. (2*b)/a
12. a*(x**2) + b*x + 1
13. (x+2*y)/(x-y)
14. (1/2)*(x**2+y**2)**0.5
15. (-2*a+(a**2+a*b)**0.5)/b
16. b**2 - 4*a*c > 0
17. 2022 < x <= 2023
18. (1/x)-x < 0
19. a = 15
20. b = 19
21. B
22. B
23. ''
24. 1
25. 4
26. 1
27. 4
28. i + j == 4
29. a = a + str(i) + str(j) + " "
30. a
31. a.replace("Thi","")
'''

#Giải thích, Test code
#Câu 3:
def cau3():
    a = 2**3 # =8
    b = 16//5 # =3
    c = 5%2 # =1
    print(a,b,c)
    print(2**3 + 16//5 + 5%2) # <=> 8 + 3 + 1 = 12 
#Câu 4 - 10:
f = 0.9
p = -0.1
q = 0.1
c = '5'
def cau4_10():
    print('4.',2*f >= 0.1) #2f = 0.18 => True
    print('5.',c == '5') #điểu hiển nhiên => True
    print('6.',p+q > 0) # -0.1 + 0.1 = 0 => False
    print('7.',abs(p) == abs(q)) # trị tuyệt đối => True
    print('8.',c < '4')

def cau11_18():
    x = 2022.5
    print('17.',2022 < x <= 2023)
#cau11_18()

def cau19_20():
    a = 1
    b = 0
    for i in range(1,6): # i lần lượt là 1, 2, 3, 4, 5
        if (i%2): #Nếu i không chia hết cho 2, ta có i = 1, 3, 5
            a *= i # a = a nhân i, tương ứng sẽ là 1, 3, 15
            b += a # b = b + a, tương ứng là 1, 4, 19
    print(a,b)
#cau19_20()
def cau21():
    a = 0
    for i in range(0,2):
        for j in range(0,3):
            a += 1
    print(a)
#cau21()
def cau22():
    a = 'Tin'
    b = 'hoc'
    print(a+" "+b)
#cau22()
def cau23_30():
    a = ''
    #Cặp i và j thỏa mãn i + j = 4, 1 <= i,j <= 3
    #Tức là ta dự đoán được là i,j sẽ nằm trong 1,3 và có thể i = 1, j = 3 (hoặc ngược lại), i,j = 2
    for i in range(1,4):
        for j in range(1,4):
            if i + j == 4:
                a = a + str(i) + str(j) + " "
    print(a)
#cau23_30()
def cau31():
    a = "Thi hoc sinh gioi"
    #Để chương trình đưa ra xâu "hoc sinh gioi"
    print(a.replace("Thi",""))
#cau31()
def cau32():
    #Tin hoc Tin hoc Tin hoc
    print(a for x in range(3): a + a)