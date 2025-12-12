def delete_item(code):
    repeat = True
    while repeat:
        code = int(input("Masukkan kode barang yang ingin dihapus: "))
        try: del barang[code]
        except KeyError:
            print("Error: Barang dengan kode tersebut tidak ditemukan!")
        else:
            print("Barang berhasil dihapus!")



    more = input("Apakah Anda ingin menghapus item lain? (y/n)")
    if more == "n":
        repeat = False
        return
    elif more == "y":
        repeat = True
    else: 
        print("Input tidak valid, kembali ke menu utama")
        repeat = False
        return
