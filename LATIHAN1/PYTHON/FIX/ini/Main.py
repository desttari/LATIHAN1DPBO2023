# import kelas mahasiswa
from Mahasiswa import Mahasiswa

# inisialisasi banyak data mahasiswa
MAX = 1000
mhs = [Mahasiswa() for i in range(MAX)]
# data kosong
count = 0

# selama belum pilih menu 5
while True:
    # menu portal
    print('\n')
    print("------------------------------------------------------------------------")
    print("------------------------------------------------------------------------")
    print("---------------SELAMAT DATANG DI PORTAL BIODATA MAHASISWA---------------")
    print("------------------------------------------------------------------------")
    print("------------------------------------------------------------------------")
    print('\n')
    print("--------------------SILAHKAN PILIH MENU DI BAWAH INI--------------------")
    print('\n')
    print("Menu:")
    print("1. Tambah Data")
    print("2. Edit Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Keluar")
    # inputan pilihan menu user
    pilihan = input("Pilihan: ")

    if pilihan == '1':  # menu tambah data
        if count == MAX:  # kalau penuh
            print("Data mahasiswa penuh.")
            print('\n')
        else:  # kalau blm
            NIM = input("Masukkan NIM: ")
            nama = input("Masukkan nama: ")
            jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")
            umur = int(input("Masukkan umur: "))
            no_hp = input("Masukkan nomor handphone: ")
            fakultas = input("Masukkan fakultas: ")
            jurusan = input("Masukkan jurusan: ")
            print('\n')

            # masukin ke temp sblm ke array
            temp = Mahasiswa()
            temp.setNIM(NIM)
            temp.setNama(nama)
            temp.setJenisKelamin(jenis_kelamin)
            temp.setUmur(umur)
            temp.setNoHP(no_hp)
            temp.setFakultas(fakultas)
            temp.setJurusan(jurusan)

            mhs[count] = temp
            count += 1  # data nambah 1

            print("Data mahasiswa berhasil ditambahkan.")
            print('\n')
    elif pilihan == '2':  # menu edit berdasar nim
        if count == 0:
            print("Belum ada data mahasiswa.")
            print('\n')
        else:
            NIM = input("Masukkan NIM yang akan diedit: ")
            # cari nim yg sama
            idx = -1
            for i in range(count):
                if mhs[i].getNIM() == NIM:
                    idx = i
                    break

            if idx == -1:
                print("Data mahasiswa dengan NIM tersebut tidak ditemukan.")
                print('\n')
            else:
                nama = input("Masukkan nama: ")
                jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")
                umur = int(input("Masukkan umur: "))
                no_hp = input("Masukkan nomor handphone: ")
                fakultas = input("Masukkan fakultas: ")
                jurusan = input("Masukkan jurusan: ")
                print('\n')

                mhs[idx].setNama(nama)
                mhs[idx].setJenisKelamin(jenis_kelamin)
                mhs[idx].setUmur(umur)
                mhs[idx].setNoHP(no_hp)
                mhs[idx].setFakultas(fakultas)
                mhs[idx].setJurusan(jurusan)

                print("Data mahasiswa berhasil diubah.")
                print('\n')
    elif pilihan == '3':  # menu hapus data berdasar nim
        if count == 0:
            print("Belum ada data mahasiswa.")
            print('\n')
        else:
            NIM = input("Masukkan NIM yang akan dihapus: ")
            # car nim yg sama
            idx = -1
            for i in range(count):
                if mhs[i].getNIM() == NIM:
                    idx = i
                    break

            if idx == -1:
                print("Data mahasiswa dengan NIM tersebut tidak ditemukan.")
                print('\n')
            else:
                for j in range(idx, count-1):
                    mhs[j] = mhs[j+1]
                count -= 1

                print("Data mahasiswa berhasil dihapus.")
                print('\n')

    elif pilihan == '4':  # menu tampilkan data
        if count == 0:
            print('\n')
            print("Belum ada data mahasiswa.")
            print('\n')
        else:
            print('\n')
            print("Data mahasiswa:")
        # ambil data trus diprint
        for i in range(count):
            print("NIM : ", mhs[i].getNIM())
            print("Nama : ", mhs[i].getNama())
            print("Jenis Kelamin : ", mhs[i].getJenisKelamin())
            print("Umur : ", mhs[i].getUmur())
            print("Nomor HP : ", mhs[i].getNoHP())
            print("Fakultas : ", mhs[i].getFakultas())
            print("Jurusan : ", mhs[i].getJurusan())
            print('\n')

    elif pilihan == '5':  # menu keluar, program berhenti
        print("------------------------------------------------------------------------")
        print("------------------------------------------------------------------------")
        print("---------------------------HAVE A NICE DAY :D---------------------------")
        print("------------------------------------------------------------------------")
        print("---------------------------------------------------------------------DLS")
        print('\n')
        break
    else:
        print('\n')
        print("Mohon pilih Menu yang tersedia")
        print('\n')
