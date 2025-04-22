class ErrorInput(Exception):
    pass

class ErrorDelete(Exception):
    pass

class ErrorNUllInput(Exception):
    pass

def TambahTugas():
    tugas = str(input("Masukkan tugas yang ingin ditambahkan: "))
    if tugas == " ":
        raise ErrorNUllInput(f"Inputan kosong.\n")
    print("Tugas berhasil ditambahkan!\n")
    return tugas

def HapusTugas(daftar_tugas):
    index = int(input("Masukkan nomor tugas yang ingin dihapus: "))
    if index < len(daftar_tugas) | index > 0:
        del daftar_tugas[index-1]
        print("Tugas berhasil dihapus!\n")
    elif index == " ":
        raise ErrorNUllInput(f"Inputan kosong.\n")
    
    else:
        raise ErrorDelete(f"Tugas dengan nomor {index} tidak ditemukan.\n")

def TampilkanDaftarTugas(daftar_tugas):
    for i in daftar_tugas:
        print (f"- {i}")

cek = True
daftar_tugas = []
while cek == True:
    try:
        print(
            "Pilih aksi:\n"
            "1. Tambah tugas\n"
            "2. Hapus tugas\n"
            "3. Tampilkan daftar tugas\n"
            "4. Keluar")

        pilih = str(input("Masukkan pilihan (1/2/3/4): "))
        if pilih == '1':
            daftar_tugas.append(TambahTugas())

        elif pilih == '2':
            HapusTugas(daftar_tugas)
            
        elif pilih == '3':
            TampilkanDaftarTugas(daftar_tugas)
            print("\n")

        elif pilih == '4':
            cek = False

        elif pilih == " ":
            raise ErrorNUllInput(f"Inputan kosong.\n")
        
        else:
            raise ErrorInput("Input tidak valid. Harap masukkan angka yang valid.\n")

    except ErrorInput as e:
        print(f"Error: {e}")

    except ErrorDelete as e:
        print(f"Error: {e}")

    except ErrorNUllInput as e:
        print(f"Error: {e}")