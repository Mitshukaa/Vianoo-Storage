#1
# R digunakan untuk Membaca File txt 
varFile = open("test.txt", "r")
print (varFile.read())
varFile.close()

#2
# readline di gunakan untuk membaca tulisan pada baris ke berapa
varFile = open("test.txt", "r")
Teks = varFile.readlines()
print (Teks[0])
print (Teks[2])
varFile.close()

#3
# Mengisi File txt ,karena adanya w yang berarti write
varFile = open("Test.txt", "w")
varFile.write("Belajar Python. \nbaca tulis file \n")
varFile.close()

#4
#Di sini menulis data siswa yang di awali menginput data.Dibawahnya program untuk memasukan Data inputan ke file txt
print ("========================================")
print ("              DATA SISWA                ")
print ("========================================")

nama = input("Nama:  ") #menginput data nama, kelas, dan alamat.Di simpan di variabel nama,kelas,alamat
kelas = input("Kelas: ")
alamat = input("Alamat: ")

#output
teks= "\nNama: {}\nKelas: {}\nAlamat: {}".format(nama, kelas, alamat,)#Data yang diinput oleh pengguna  akan ditampilkan.
File_Data = open("Test.txt", "r+")
File_Data.write(teks)
File_Data.close()

