barang = {}
user_choice_loop = True
main_loop = True

def show_items():
    for i in range(5):
        print(i)

def add_item(code, name, stock):
    print("addItem")

def update_item(code, name = None, stock = None):
    print("updateItem")

def delete_item(code):
    print("deleteItem")

print("===== PILIH MENU =====")
print("1. Tambah Barang")
print("2. Lihat Barang")
print("3. Update Barang")
print("4. Hapus Barang")
print("5. Keluar")
print("=======================")


while main_loop:
    while user_choice_loop:
        user_choice = input("Pilih menu (1/2/3/4): ")
        if user_choice not in ("1", "2", "3", "4", "5"):
            print("Menu tidak tersedia")
        else:
            user_choice_loop = False

    match user_choice:
        case "1":
            show_items()
        case "2":
            add_item()
        case "3":
            update_item()
        case "4":
            delete_item()
        case "5":
            main_loop = False




