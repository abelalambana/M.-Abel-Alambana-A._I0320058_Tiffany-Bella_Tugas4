#Tulis beberapa kode untuk memeriksa berat bagasi Anda di konter check-in 
# maskapai. Anggaplah berat maksimum yang diperbolehkan adalah 50 lbs. 
# apa yang terjadi apabila:

lbs_50=0.45*50 

#a. Berat lebih 110 kg
#Output false
a=110
print('Apakah boleh berat bagasi lebih dari 110 kg ?', a<lbs_50)

#b. Berat 49 kg
b=49
print('Apakah boleh berat bagasi samadengan 49 kg ?', lbs_50>b)

