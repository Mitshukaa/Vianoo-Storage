print ("========================================")
print ("                WELCOME                 ")
print ("========================================")

nama = input("Nama:  ") #input
kelas = input("Kelas: ")
alamat = input("Alamat: ")


#output
teks= "\nNama: {}\nKelas: {}\nAlamat: {}".format(nama, kelas, alamat,) #Data yang diinput oleh pengguna  akan ditampilkan.
File_Data = open("readwrite.txt", "w")#membuka file readwrite.txt dalam mode write.
File_Data.write(teks)
File_Data.close()

File_Data = open("readwrite.txt", "r") #membuka file readwrite.txt dalam mode baca.
Baca = File_Data.read()
print(Baca)
File_Data.close()
