#dec to bin
def dec_to_bin(num):
    return bin(num).replace("0b", "")

#bin to dec
def bin_to_dec(num):
    try:
        result = int(num, 2)
    except TypeError:
        num = str(num)
        result = int(num, 2)
    return result

#cong nhi phan
def plus_binary(num1, num2):
    x = bin_to_dec(num1)
    y = bin_to_dec(num2)
    dec = x + y
    result = dec_to_bin(dec)
    return result

binary = int(input("bin: "))
decimal = int(input("dec: "))

bin1 = int(input("bin1: "))
bin2 = int(input("bin2: "))

print(dec_to_bin(decimal),bin_to_dec(binary),plus_binary(bin1, bin2))