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

# Sorting harga barang
daftar_harga_produk = [item[2] for item in cart]
daftar_produk = [item[0] for item in cart]
jumlah_barang = len(daftar_harga_produk)

for i in range(jumlah_barang):
    for j in range(jumlah_barang - i - 1):
        if daftar_harga_produk[j] > daftar_harga_produk[j + 1]:
            daftar_harga_produk[j], daftar_harga_produk[j + 1] = daftar_harga_produk[j + 1], daftar_harga_produk[j]
            daftar_produk[j], daftar_produk[j + 1] = daftar_produk[j + 1], daftar_produk[j]

print("\nDaftar Produk Diurutkan Berdasarkan Harga :")
print("\n=================== DAFTAR PRODUK YANG DIBELI ===================")
for i in range(jumlah_barang):
    print(daftar_produk[i], "- Rp", daftar_harga_produk[i])
print("=================================================================")