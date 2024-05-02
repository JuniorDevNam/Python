ss = float(input("Nhập số giây: "))

def cach1(ss):
    #Số ngày
    ngay=ss//86400
    #Giây chia cho 3600 ra tổng số giờ rồi trừ đi số giờ trong số ngày
    gio=ss//3600-ngay*24

    phut=ss//60-ngay*24*60-gio*60

    giay=ss-ngay*24*3600-gio*3600-phut*60

    return "Số giây đã nhập là: "+str(int(ss))+" tương đương với: "+str(int(ngay))+" ngày "+str(int(gio))+" giờ "+str(int(phut))+" phút "+str(int(giay))+" giây."
def cach2(ss):
    ngay = int(ss/86400)
    ngay2 = float(ss/86400)
    ngaydu = float(ngay2 - ngay)

    gio = int(ngaydu*24)
    gio2 = float(ngaydu*24)
    giodu = float(gio2 - gio)

    phut = int(giodu*60)
    phut2 = float(giodu*60)
    phutdu = float(phut2 - phut)

    giay = float(phutdu*60)

    return "Số giây đã nhập là: "+str(ss)+" tương đương với: "+str(ngay)+" ngày "+str(gio)+" giờ "+str(phut)+" phút "+str(giay)+" giây."

kq1 = cach1(ss)
kq2 = cach2(ss)
print("Cách 1: ",kq1)
print("Cách 2: ",kq2)

#print("Số giây bạn đã nhập là:", ss,",tương đương với:",ngay,"ngày,",int(gio),"giờ,",int(phut),"phút",int(giay),"giây")