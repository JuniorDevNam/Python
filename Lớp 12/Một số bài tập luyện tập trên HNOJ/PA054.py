'''
https://hnoj.edu.vn/problem/pa054
Cho một số tự nhiên n.
Hãy in ra màn hình các chữ số của n trên các dòng khác nhau theo cách viết sau

Số 0 được viết như sau:

###
#.#
#.#
#.#
###

Số 1 được viết như sau:

..#
.##
#.#
..#
..#

Số 2 được viết như sau:

###
..#
.#.
#..
###

Số 3 được viết như sau:

###
..#
###
..#
###
'''
n = int(input())

khong = '''###
#.#
#.#
#.#
###
'''
mot = '''..#
.##
#.#
..#
..#
'''
hai = '''###
..#
.#.
#..
###
'''
ba = '''###
..#
###
..#
###
'''
for x in str(n):
    if x == "0":
        print(khong)
    if x == "1":
        print(mot)
    if x == "2":
        print(hai)
    if x == "3":
        print(ba)