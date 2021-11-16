nama_pembeli = input("Masukan Nama Anda : ")
print("\n===========================================")
print("Pilihan Produk")
print("[1] Kipas Angin  -> Rp. 1.000.000/unit")
print("[2] TV \t\t -> Rp. 2.000.000/unit")
print("[3] Mesin Cuci \t -> Rp. 3.000.000/unit")
print("[4] AC \t\t -> Rp. 4.000.000/unit")
print("[5] Kulkas \t -> Rp. 5.000.000/unit")

pilihan = int(input("\npilihan\t: "))
if pilihan == 1:
    nama_produk = "Kipas Angin"
    harga = 1000000
elif pilihan == 2:
    nama_produk ="TV"
    harga = 2000000
elif pilihan == 3:
    nama_produk = "Mesin Cuci"
    harga = 3000000
elif pilihan == 4:
    nama_produk = "AC"
    harga = 4000000
elif pilihan == 5:
    nama_produk = "Kulkas"
    harga = 5000000
else: 
    harga = 0 
jumlah_beli = int(input("Jumlah Beli : "))

harga_kotor = harga * jumlah_beli

if pilihan == 1 and jumlah_beli >= 5:
    diskon = harga_kotor * (20/100)
elif pilihan == 4 and jumlah_beli >= 3:
    diskon = harga_kotor * (10/100)
else:
    diskon = harga_kotor * (5/100)

ppn = (harga_kotor - diskon) * (10/100)

harga_bersih = harga_kotor - diskon + ppn

print ("=========================")
print ("Nama Pelanggan \t:", nama_pembeli)
print ("Produk Pilihan \t:", nama_produk)
print ("Harga Produk \t:", harga)
print ("Jumlah Beli \t:", jumlah_beli)
print ("Harga Kotor \t:", harga_kotor)
print ("Diskon \t\t:", diskon)
print ("PPN \t\t:", ppn)
print ("Harga Bersih \t:", harga_bersih)