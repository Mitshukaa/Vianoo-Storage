#Di sini menulis data siswa yang di awali menginput data .Dibawahnya program untuk memasukan Data inputan ke file txt
print ("========================================")
print ("               Mereplace                ")
print ("========================================")

nama = input("Nama:  ") #menginput data nama, kelas, dan alamat.Di simpan di variabel nama,kelas,alamat
kelas = input("Kelas: ")
alamat = input("Alamat: ")
print ("========================================")
nama2 = input("Nama:  ") #menginput data nama, kelas, dan alamat.Di simpan di variabel nama,kelas,alamat
kelas2 = input("Kelas: ")
alamat2 = input("Alamat: ")

#output
teks= "\nNama: {}\nKelas: {}\nAlamat: {}\nNama: {}\nKelas: {}\nAlamat: {}".format(nama, kelas, alamat,nama2, kelas2, alamat2) #Data yang diinput oleh pengguna pada bagian pertama akan ditampilkan terlebih dahulu, diikuti dengan data yang diinput pada bagian kedua.
File_Data = open("mereplace.txt", "w")
File_Data.write(teks)
File_Data.close()