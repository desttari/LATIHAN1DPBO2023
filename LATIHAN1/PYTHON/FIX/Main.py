from DaftarMahasiswa import DaftarMahasiswa
from Mahasiswa import Mahasiswa


def main():
    print("Me:")
    daftar_mahasiswa = DaftarMahasiswa()

    while True:
        print("Menu:")
        print("1. Tambah Mahasiswa")
        print("2. Ubah Mahasiswa")
        print("3. Hapus Mahasiswa")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            prog_studi = input("Masukkan program studi mahasiswa: ")
            fakultas = input("Masukkan fakultas mahasiswa: ")
            umur = input("Masukkan umur mahasiswa: ")
            email = input("Masukkan email mahasiswa: ")
            mahasiswa = Mahasiswa(nama, nim, prog_studi, fakultas, umur, email)
            daftar_mahasiswa.tambah_mahasiswa(mahasiswa)
            print("Mahasiswa berhasil ditambahkan.")
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
            for mahasiswa in daftar_mahasiswa.list_mahasiswa:
                if mahasiswa.nim == nim:
                    print("Data Mahasiswa:")
                    print("Nama: ", mahasiswa.nama)
                    print("NIM: ", mahasiswa.nim)
                    print("Program Studi: ", mahasiswa.prog_studi)
                    print("Fakultas: ", mahasiswa.fakultas)
                    print("Umur: ", mahasiswa.umur)
                    print("Email: ", mahasiswa.email)

                    nama = input(
                        "Masukkan nama baru (kosongkan jika tidak ingin diubah): ")
                    prog_studi = input(
                        "Masukkan program studi baru (kosongkan jika tidak ingin diubah): ")
                    fakultas = input(
                        "Masukkan fakultas baru (kosongkan jika tidak ingin diubah): ")
                    umur = input(
                        "Masukkan umur baru (kosongkan jika tidak ingin diubah): ")
                    email = input(
                        "Masukkan email baru (kosongkan jika tidak ingin diubah): ")

                    # Membuat objek Mahasiswa baru dengan nilai-nilai yang diperbarui
                    new_mahasiswa = Mahasiswa(
                        nama if nama != "" else mahasiswa.nama,
                        nim,
                        prog_studi if prog_studi != "" else mahasiswa.prog_studi,
                        fakultas if fakultas != "" else mahasiswa.fakultas,
                        umur if umur != "" else mahasiswa.umur,
                        email if email != "" else mahasiswa.email
                    )

                    daftar_mahasiswa.ubah_mahasiswa(nim, new_mahasiswa)
                    break
                else:
                    print("Tidak ditemukan mahasiswa dengan NIM {}.".format(nim))
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            daftar_mahasiswa.hapus_mahasiswa(nim)
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
