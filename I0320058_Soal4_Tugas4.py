#Untuk mendaftar pada kursus online,
# calon siswa harus berusia minimal 21 tahun dan telah lulus ujian kualifikasi. 
# Pengguna akan ditanyai pertanyaan-pertanyaan berikut:

print('=================================================')
print('Program Kelayakan Mengikuti Kursus')
print('=================================================')

a= int(input('Berapa umur anda ? '))

if a >= 21:
    c=(input('Apakah Anda sudah lulus ujian kualifikasi (Y / T)? ').upper())
    if c== 'Y':
        print('Anda Dapat Mendaftar di Kursus')
    elif c== 'T':
        print('Anda Tidak Dapat Mendaftar di Kursus')
    else:
        print('Input Error')
elif a<= 21:
    print('Anda Tidak Dapat Mendaftar di Kursus')
else:
    print('Input Error')

