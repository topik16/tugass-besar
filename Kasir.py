
# Memperbarui daftar barang setelah pembelian
def update_daftar_barang(nama_barang, jumlah_beli):
    for barang in daftar_barang:
        if barang["nama"] == nama_barang:
            barang["jumlah"] = barang.get("jumlah", 0) + jumlah_beli

# Shopping cart
cart = []

def tambah_barang():
    fungsibelanja()
    cart.append((barang, jumlah, totalblj))
    update_daftar_barang(barang, jumlah)

# Melihat daftar barang dalam keranjang
def lihat_barang():
    print("\n=================== DAFTAR PRODUK DALAM KERANJANG ===================")
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

# Melakukan sorting daftar barang berdasarkan harga
def sorting_harga_barang():
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
    print("=================================================================")

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
