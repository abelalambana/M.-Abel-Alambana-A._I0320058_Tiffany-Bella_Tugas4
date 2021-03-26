#4 adalah 100 dalam biner dan 11 adalah 1011. 
# Apa keluaran dari operator bitwise berikut?

a=4
b=11
print('biner dari', a,' adalah',format(a, '08b'))
print('biner dari', b,' adalah',format(b, '08b'))
print(' ')

#a. 4 | 11
print('=================(4|11)=================')
print('biner dari', a,' adalah',format(a, '08b'))
print('biner dari', b,' adalah',format(b, '08b'))
print('==========================================(|)')
print('nilai :', a|b, ' angka binernya :',format(a|b, '08b'))
print(' ')

#b. 4 >> 11
print('=================(4>>11)=================')
print('biner dari', a,' adalah',format(a, '08b'))
print('biner dari', b,' adalah',format(b, '08b'))
print('==========================================(>>)')
print('nilai :', a>>b, ' angka binernya :',format(a>>b, '08b'))
print(' ')

#c. 4 ^ 11
print('=================(4^11)=================')
print('biner dari', a,' adalah',format(a, '08b'))
print('biner dari', b,' adalah',format(b, '08b'))
print('==========================================(^)')
print('nilai :', a^b, ' angka binernya :',format(a^b, '08b'))
print(' ')

#d. ~4
print('=================(~4)=================')
print('biner dari', a,' adalah',format(a, '08b'))
print('==========================================(~)')
print('nilai :', ~a, ' angka binernya :',format(~a, '08b'))
print(' ')

#e. 11 & 4
print('=================(11&4)=================')
print('biner dari', b,' adalah',format(b, '08b'))
print('biner dari', a,' adalah',format(a, '08b'))
print('==========================================(&)')
print('nilai :', b&a, ' angka binernya :',format(b&a, '08b'))
print(' ')