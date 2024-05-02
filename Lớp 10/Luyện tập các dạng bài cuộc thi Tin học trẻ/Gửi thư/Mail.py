'''
Cho N là số học sinh nhập từ bàn phím.
Các học sinh này mỗi người muốn gửi bài của mình cho nhau.
Hãy tính số lần gửi thư sao cho tất cả học sinh đều nhận được 
tất cả các bài của những học sinh khác.

Ví dụ: Có 3 học sinh. Người 1 gửi cho người 3 bài của người 1, 
người 2 gửi cho người 3 bài của người 2,
người 3 gửi cho người 1 bài của người 3 với bài của người 2,
người 3 gửi cho người 2 bài của người 3 với bài của người 1.
Tổng 4 lần gửi thư.
'''

# Phân tích ta thấy là sẽ có 1 người chuyên nhận của tất cả mọi người khác và
#sau đó chuyển tiếp bài của những người khác và của mình cho từng người sao cho mỗi người đều có
#bài của những người khác. Ta coi như người này là 'monitor' và những
# người khác là 'others' đi.

N = int(input("Nhập số học sinh: ")) #Số học sinh tương đương với tổng số bài
#Số học sinh = tổng số bài 
others = N-1 #N-1 đứa khác gửi cho monitor (vì không tính monitor) = tổng số lần gửi 1
monitor = others #monitor gửi lại cho những đứa kia mỗi đứa bài của những đứa còn lại và bài của monitor
# = tổng số lần gửi 2
tongthu1 = others + monitor

print(tongthu1)

# Trường hợp 2 (Không thấy khớp với ví dụ đề bài cho) đó là từng người 1 gửi chéo cho nhau
# Phân tích:
#Mỗi người sẽ gửi đi N-1 lần cho N-1 người còn lại
#Ví dụ với N = 3: 
#học sinh 1, 2, 3 tương ứng là x, y, z
#x = 2 vì gửi cho y và z
#y = 2 vì gửi cho x và z
#z = 2 vì gửi cho x và y
#Với 3 người và mỗi người 2 lần ta có tổng 6 lần
#Thế với những số lớn hơn thì sao?
#Với N = 50:
#ng 1 = 49 lần gửi
#ng 2 = 49 lần gửi
#...
#ng 49 = 49 lần gửi
#ng 50 = 49 lần gửi
#Vậy suy ra ta có công thức như sau:
tongthu2 = N*(N-1)
print(tongthu2) #Check đáp án với N = 3 sẽ thấy thỏa mãn ví dụ của TH2