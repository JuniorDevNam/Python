# Viết chương trình nhập vào 1 dãy số ngẫu nhiên từ bàn phím, 
# in ra các số chẵn dương và vị trí của chúng.

spt = int(input("Nhập số phần tử muốn có trong dãy số: "))
dso = []
for x in range(spt):
  dso.append(float(input("Nhập số bất kỳ thứ "+str(x+1)+":")))
  
for i in range(spt):
  if dso[i]%2==0 and dso[i]>0:
    print("Số chẵn dương là:",dso[i],"ở vị trí",i,"trong dãy số")