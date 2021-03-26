#Tulis program yang meminta pengguna memasukkan dua bilangan bulat. 
# Minta output program berapa kali angka kedua dapat dibagi menjadi angka pertama. 
# Misalnya jika angka pertama yang dimasukkan adalah 23 dan angka kedua yang dimasukkan adalah 4, 
# program harus melaporkan 5 kali (angka dibelakang koma diabaikan). 
# Anda diharuskan untuk mengimplementasikan program ini menggunakan operator floor!

a= int(input('Masukkan Angka Pertama yang diinginkan : '))
b= int(input('Masukkan Angka Kedua yang diinginkan : '))

print ('Angka pertama dapat dibagi dengan angka kedua sebanyak {} kali'.format(a//b))

