produk = {
    "Laptop": 5500000, 
    "Smartphone": 3000000, 
    "Tablet": 2000000, 
    "Smartwatch": 1500000, 
    "Headphone": 500000 
} 

def cek_penawaran(tawaran):
    if tawaran < 80/100:
       harga_barang = tawaran
       return harga_barang
    else:
        return "Penawaran ditolak. Harga asli digunakan."

def hitung_diskon(pembelian):   
    if pembelian > 10000000:
        diskon = 10
        return diskon
    elif pembelian > 500000:
        diskon = 5
        return diskon
    else:
        diskon = 0
        return diskon

def transaksi(nama, produk, jumlah, harga, diskon, totalakhir):
    print("==== STRUK PEMBELIAN ====")
    print(f"Nama Pembeli : {nama}")
    print(f"Produk Dibeli: {produk}")
    print(f"Jumlah Unit  : {jumlah}")
    print(f"Harga/Unit   : {harga}")
    print(f"Subtotal     : {harga}")
    print(f"Diskon       : {diskon}%")
    print(f"Total Akhir  : {totalakhir}")
    print("===============================")

while True:
    print("Masukkan Data")
    nama = input("Nama : ")
    umur = int(input("Umur : "))
    member = input("Apakah pelanggan member? (ya/tidak) ")
    print("Daftar Produk")
    for key, values in produk.items():
        print(f"- {key} - Harga : Rp.{values}")

    pilihan = input("Pilih Pembelian : ")

    if member == "ya":
        diskon = hitung_diskon(values)

    if umur < 17 and values > 3000000:
        print("Maaf, Anda belum cukup umur untuk membeli produk ini.")
        break

    jumlah = int(input("Masukkan jumlah : "))
    
    penawaran = input("Apakah ingin melakukan penawaran? (ya/tidak) ")

    if penawaran == "ya":
        tawaran = int(input("Masukkan harga tawaran : "))
        cek_penawaran(tawaran)

    diskon = 0

    harga = int(values)
    totalakhir = harga * jumlah
    transaksi(nama, pilihan, jumlah, harga, diskon, totalakhir)

    selesai = input("Ingin melakukan pembelian lain? (ya/tidak)")

    if selesai != "ya":
        break