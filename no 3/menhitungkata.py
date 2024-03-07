file = open("jumlahkata.txt",) #membuka file txt
isi = file.read() #membaca isi file jumlahkata.txt dan menyimpannya ke dalam variabel isi
hitung = dict() #membuat kamus kosong bernama hitung.
line = isi
kata = line.split() # memecah isi file
for word in kata : #memulai perulangan untuk setiap kata dalam daftar kata
    hitung[word] = hitung.get(word,0) + 1

#output
for key, value in hitung.items():
    print(key, ":", value)

