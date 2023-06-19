print("========================================")
print("            GROSIR MARKET               ")
print("========================================")
pembeli = input("Masukkan nama Pembeli: ")
print("Nama Pembeli :", pembeli)
print("========================================")
def fungsibelanja():
    global totalblj
    global jumlah
    global barang
    print("\n<================== SEMBAKO =====================>")
    print("DAFTAR PRODUK")
    print("1. Minyak Goreng - Rp 15000")
    print("2. Garam - Rp 9000")
    print("3. Beras - Rp 10000")
    print("4. Telur  - Rp 7500")
    print("5. Gula Pasir - Rp 9000")
    print("6. Penyedap Makanan - Rp 2000")
    print("7. Bawang Merah - Rp 12000")
    print("8. Bawang Putih - Rp 12000")
    print("9. Mentega - Rp 3500")
    nomor = int(input("Masukan Pilihan: "))
    jumlah = int(input("Jumlah: "))
    
    if nomor == 1:
        totalblj = jumlah * 15000
        print(jumlah, " Jumlah = Rp", totalblj)
        barang = "Minyak Goreng"
    elif nomor == 2:
        totalblj = jumlah * 9000
        print(jumlah, " JUmlah = Rp", totalblj)
        barang = "Garam"
    elif nomor == 3:
        totalblj = jumlah * 11000
        print(jumlah, " Berapa Kilo = Rp", totalblj)
        barang = "Beras"
    elif nomor == 4:
        totalblj = jumlah * 7500
        print(jumlah, "Jumlah = Rp", totalblj)
        barang = "Telur"
    elif nomor == 5:
        totalblj = jumlah * 9000
        print(jumlah, "Jumlah = Rp", totalblj)
        barang = "Gula Pasir"
    elif nomor == 6:
        totalblj = jumlah * 2000
        print(jumlah, "Jumlah = Rp", totalblj)
        barang = "Penyedap Makanan"
    elif nomor == 7:
        totalblj = jumlah * 12000
        print(jumlah, "Jumlah = Rp", totalblj)
        barang = "Bawang Merah"
    elif nomor == 8:
        totalblj = jumlah * 12000
        print(jumlah, "Jumlah = Rp", totalblj)
        barang = "Bawang Putih"
    elif nomor == 9:
        totalblj = jumlah * 12000
        print(jumlah, "Jumlah = Rp", totalblj)
        barang = "Mentega"
    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!")
        fungsibelanja()

# Shopping cart
cart = []

fungsibelanja()
cart.append((barang, jumlah, totalblj))

while True:
    tambah_barang = input("Tambahkan barang lain? (y/n): ")
    if tambah_barang.lower() == "y":
        fungsibelanja()
        cart.append((barang, jumlah, totalblj))
    else:
        break

totalsemua = sum(item[2] for item in cart)

print("\nTotal Harus Dibayar: Rp", totalsemua)
uang = int(input("Uang Tunai Pembeli: Rp "))
kembalian = int(uang - totalsemua)
print("Kembalian :", kembalian)

print("\n================================================")
print("========== S T R U K   B E L I =================")
print("================================================")
print("Nama\t\t:", pembeli)
for item in cart:
    print("Beli\t\t:", item[1], item[0], "( Rp", item[2], ")")
print("Tagihan\t\t: Rp", totalsemua)
print("Dibayar\t\t: Rp", uang)
print("Kembalian\t: Rp", kembalian)
print("================================================")
print("================================================")

# Searching barang
def searching_produk(nama_barang):
    daftar_barang = ["Minyak Goreng", "Garam", "Beras", "Telur", "Gula Pasir", "Penyedap Makanan", "Bawang Merah", "Bawang Putih", "Mentega"]
    if nama_barang in daftar_barang:
        return True
    else:
        return False

nama_barang = input("\nMasukkan nama barang yang ingin dicari: ")
if searching_produk(nama_barang):
    print("Barang", nama_barang, "tersedia di menu.")
else:
    print("Barang", nama_barang, "tidak tersedia di menu.")


# Sorting harga barang
daftar_harga_produk = [item[2] for item in cart]
daftar_produk = [item[0] for item in cart]
jumlah_barang = len(daftar_harga_produk)

for i in range(jumlah_barang):
    for j in range(jumlah_barang - i - 1):
        if daftar_harga_produk[j] > daftar_harga_produk[j + 1]:
            daftar_harga_produk[j], daftar_harga_produk[j + 1] = daftar_harga_produk[j + 1], daftar_harga_produk[j]
            daftar_produk[j], daftar_produk[j + 1] = daftar_produk[j + 1], daftar_produk[j]

print("\nDaftar Produk Setelah Diurutkan Berdasarkan Harga :")
print("\n=================== DAFTAR PRODUK YANG DIBELI ===================")
for i in range(jumlah_barang):
    print(daftar_produk[i], "- Rp", daftar_harga_produk[i])
print("==================================================================")
