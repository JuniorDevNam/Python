n = int(input('Nhap so luong n nguoi can nhap: '))
ds = []
for i in range(n):
        ho_ten = input("Nhập họ tên của người thứ {}:".format(i + 1))
        tuoi = int(input("Nhập tuổi của người thứ {}:".format(i + 1)))
        gioi_tinh = input("Nhập giới tính của người thứ {}:".format(i + 1))
        que_quan = input("Nhập quê quán của người thứ {}:".format(i + 1))

        nguoi = {
            "Họ tên": ho_ten,
            "Tuổi": tuoi,
            "Giới tính": gioi_tinh,
            "Quê quán": que_quan
        }
        ds.append(nguoi)
for stt, ng in enumerate(ds):
    print("Thong tin nguoi thu {} la: ".format(stt+1))
    for tt, gt in nguoi.items():
        print('{}: {}'.format(tt, gt))
