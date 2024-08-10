# Bài 10: VCT giải hai bài toán cổ: 100 trâu 100 bó cỏ và vừa gà vừa chó 36 con 100 chân?
def giai_bai_toan_trau():
    for x in range(21):  # Trâu đứng ăn 5 bó cỏ, tối đa 20 con
        for y in range(34):  # Trâu nằm ăn 3 bó cỏ, tối đa 33 con
            z = 100 - x - y
            if 5 * x + 3 * y + z == 100:
                print(f"Trâu đứng: {x}, Trâu nằm: {y}, Trâu già: {z}")

giai_bai_toan_trau()

def giai_bai_toan_ga_cho():
    for x in range(37):  # Số gà tối đa là 36
        y = 36 - x
        if 2 * x + 4 * y == 100:
            print(f"Số gà: {x}, Số chó: {y}")

giai_bai_toan_ga_cho()