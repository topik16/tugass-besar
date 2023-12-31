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

daftar_barang.sort(key=lambda x: x["nama"])

# Searching barang
def searching_produk(nama_barang):
    for barang in daftar_barang:
        if barang["nama"].lower() == nama_barang.lower():
            return barang
    return None

def get_harga_barang(nama_barang):
    barang = searching_produk(nama_barang)
    if barang:
        return barang["harga"]
    else:
        return None

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
    pilihan = input("Masukkan Nama Barang atau Nomor Barang: ")
    jumlah = int(input("Jumlah: "))

    # jika pilihan adalah angka
    if pilihan.isdigit():
        nomor = int(pilihan)
        if 1 <= nomor <= len(daftar_barang):
            barang = daftar_barang[nomor - 1]
            harga_barang = barang["harga"]
            totalblj = jumlah * harga_barang
            print(jumlah, " Jumlah = Rp", totalblj)
        else:
            print("Pilihan tidak ada, silakan masukan lagi!!")
            fungsibelanja()
    else:
        barang = searching_produk(pilihan)
        if barang:
            harga_barang = barang["harga"]
            totalblj = jumlah * harga_barang
            print(jumlah, " Jumlah = Rp", totalblj)
        else:
            print("Barang tidak ditemukan. Silakan coba lagi!")
            fungsibelanja()

# Memperbarui daftar barang setelah pembelian
def update_daftar_barang(nama_barang, jumlah_beli):
    for barang in daftar_barang:
        if barang["nama"].lower() == nama_barang.lower():
            barang["jumlah"] = barang.get("jumlah", 0) + jumlah_beli

cart = []

def tambah_barang():
    fungsibelanja()
    cart.append((barang["nama"], jumlah, totalblj))
    update_daftar_barang(barang["nama"], jumlah)

# Melihat daftar barang dalam keranjang
def lihat_pesanan():
    print("\n=================== DAFTAR PRODUK YANG DIBELI  ===================")
    for item in cart:
        print(item[0], "- Jumlah:", item[1], "- Harga: Rp", item[2])
    print("=====================================================================")

# Melakukan pencarian nama barang
def cari_barang():
    nama_barang = input("\nMasukkan nama barang yang ingin dicari: ")
    barang = searching_produk(nama_barang)
    if barang:
        print("Barang", barang["nama"], "tersedia di menu dengan harga Rp", barang["harga"])
    else:
        print("Barang", nama_barang, "tidak tersedia di menu.")

# Melakukan sorting daftar barang berdasarkan harga dengan bubble sort
def sorting_harga_barang():
    daftar_harga_produk = [item[2] for item in cart]
    daftar_produk = [item[0] for item in cart]
    jumlah_barang = len(daftar_harga_produk)

    for i in range(jumlah_barang):
        for j in range(jumlah_barang - i - 1):
            if daftar_harga_produk[j] > daftar_harga_produk[j + 1]:
                daftar_harga_produk[j], daftar_harga_produk[j + 1] = daftar_harga_produk[j + 1], daftar_harga_produk[j]
                daftar_produk[j], daftar_produk[j + 1] = daftar_produk[j + 1], daftar_produk[j + 1], daftar_produk[j]

    print("\nDaftar Produk Setelah Diurutkan Berdasarkan Harga :")
    print("\n=================== DAFTAR PRODUK YANG DIBELI ===================")
    for i in range(jumlah_barang):
        print(daftar_produk[i], "- Rp", daftar_harga_produk[i])
    print("=================================================================")

# Menghapus barang dari keranjang
def hapus_barang():
    if len(cart) == 0:
        print("Keranjang belanja kosong.")
    else:
        lihat_pesanan()
        index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
        if index >= 0 and index < len(cart):
            print("Anda akan menghapus barang", cart[index][0])
            konfirmasi = input("Apakah Anda yakin ingin menghapus barang tersebut? (ya/tidak): ")
            if konfirmasi.lower() == "ya":
                deleted_item = cart.pop(index)
                deleted_items.append(deleted_item)
                print("Barang", deleted_item[0], "dengan jumlah", deleted_item[1], "telah dihapus dari keranjang.")
            else:
                print("Penghapusan barang dibatalkan.")
        else:
            print("Nomor barang tidak valid.")

def batalkan_hapus():
    global deleted_items
    if len(deleted_items) == 0:
        print("Tidak ada barang yang dihapus untuk dibatalkan.")
    else:
        print("\n==================== BARANG YANG DIHAPUS ====================")
        for i, item in enumerate(deleted_items):
            print(f"{i+1}. {item[0]} - Jumlah: {item[1]} - Harga: Rp {item[2]}")
        index = int(input("Masukkan nomor barang yang ingin dibatalkan penghapusan: ")) - 1
        if index >= 0 and index < len(deleted_items):
            restored_item = deleted_items.pop(index)
            cart.append(restored_item)
            print("Barang", restored_item[0], "dengan jumlah", restored_item[1], "telah dibatalkan penghapusannya.")
        else:
            print("Nomor barang tidak valid.")

# Variabel global
totalblj = 0
jumlah = 0
barang = ""

deleted_items = []

while True:
    print("\n<====================== MENU ========================>")
    print("1. Tambah Barang")
    print("2. Lihat Pesanan")
    print("3. Hapus Barang")
    print("4. Batalkan Penghapusan Barang")
    print("5. Cari Barang")
    print("6. Sorting Harga Barang")
    print("7. Selesai Belanja")
    menu = input("Pilih menu: ")

    if menu == "1":
        tambah_barang()
    elif menu == "2":
        lihat_pesanan()
    elif menu == "3":
        hapus_barang()
    elif menu == "4":
        batalkan_hapus()
    elif menu == "5":
        cari_barang()
    elif menu == "6":
        sorting_harga_barang()
    elif menu == "7":
        break
    else:
        print("Menu tidak valid. Silakan pilih kembali.")

totalsemua = sum(item[2] for item in cart)

print("\nTotal Harus Dibayar: Rp", totalsemua)
uang = int(input("Uang Tunai Pembeli: Rp "))
kembalian = int(uang - totalsemua)

import sys
while True:
    if uang < totalsemua:
        print("\nUang tidak cukup untuk membayar belanjaan.")
        print("Belanjaan belum lunas.")

        ulang = input("Apakah Anda ingin mengulang pembayaran? (ya/tidak): ")
        if ulang.lower() == "tidak":
            sys.exit("Program dihentikan.")
        elif ulang.lower() == "ya":
            uang = int(input("Uang Tunai Pembeli: Rp "))
            kembalian = uang - totalsemua
            continue
        else:
            print("Opsi tidak valid. Silakan pilih 'ya' atau 'tidak'.")
    else:
        print("\nBelanjaan telah lunas.")
        break


print("\n=======================================================")
print("========== S T R U K   P E M B E L I A N ==============")
print("=======================================================")
print("Nama\t\t:", pembeli)
for item in cart:
        print("Beli\t\t:", item[1], item[0], "( Rp", item[2], ")")
print("Tagihan\t\t: Rp", totalsemua)
print("Dibayar\t\t: Rp", uang)
print("Kembalian\t: Rp", kembalian)
print("======================================================")
print("======================================================")
