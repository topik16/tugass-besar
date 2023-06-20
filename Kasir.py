# Program utama
print("========================================")
print("            GROSIR MARKET               ")
print("========================================")
pembeli = input("Masukkan Nama Pembeli: ")
print("Nama Pembeli :", pembeli)


# Array untuk daftar barang
daftar_barang = [
    {"nama": "Minyak Goreng", "harga": 15000},
    {"nama": "Garam", "harga": 9000},
    {"nama": "Beras", "harga": 10000},
    {"nama": "Telur", "harga": 7500},
    {"nama": "Gula Pasir", "harga": 9000},
    {"nama": "Penyedap Makanan", "harga": 2000},
    {"nama": "Bawang Merah", "harga": 12000},
    {"nama": "Bawang Putih", "harga": 12000},
    {"nama": "Mentega", "harga": 3500}
]

# Searching barang
def searching_produk(nama_barang):
    for barang in daftar_barang:
        if barang["nama"] == nama_barang:
            return barang
    return None

# Mendapatkan harga barang dari nama barang
def get_harga_barang(nama_barang):
    barang = searching_produk(nama_barang)
    if barang:
        return barang["harga"]
    else:
        return None

# Mendapatkan nama barang dari harga barang
def get_nama_barang(harga_barang):
    for barang in daftar_barang:
        if barang["harga"] == harga_barang:
            return barang["nama"]
    return None

# Fungsi untuk melakukan pembelian barang
def fungsibelanja():
    global totalblj
    global jumlah
    global barang
    print("\n<================== SEMBAKO =====================>")
    print("DAFTAR PRODUK")
    for i, barang in enumerate(daftar_barang, start=1):
        print(f"{i}. {barang['nama']} - Rp {barang['harga']}")
    nomor = int(input("Masukkan Pilihan: "))
    jumlah = int(input("Jumlah: "))

    if 1 <= nomor <= len(daftar_barang):
        harga_barang = daftar_barang[nomor - 1]["harga"]
        totalblj = jumlah * harga_barang
        print(jumlah, " Jumlah = Rp", totalblj)
        barang = daftar_barang[nomor - 1]["nama"]
    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!")
        fungsibelanja()
