class Mahasiswa:
    def __init__(self, nama, nim, prog_studi, fakultas, umur, email):
        self.nama = nama
        self.nim = nim
        self.prog_studi = prog_studi
        self.fakultas = fakultas
        self.umur = umur
        self.email = email


class DaftarMahasiswa:
    def __init__(self):
        self.list_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.list_mahasiswa.append(mahasiswa)

    def ubah_mahasiswa(self, index, mahasiswa):
        self.list_mahasiswa[index] = mahasiswa

    def hapus_mahasiswa(self, index):
        self.list_mahasiswa.pop(index)

    def tampilkan_daftar(self):
        print("Daftar Mahasiswa:")
        print("{:<20} {:<15} {:<25} {:<20} {:<5} {:<25}".format(
            "Nama", "NIM", "Program Studi", "Fakultas", "Umur", "Email"))
        for mahasiswa in self.list_mahasiswa:
            print("{:<20} {:<15} {:<25} {:<20} {:<5} {:<25}".format(mahasiswa.nama, mahasiswa.nim,
                  mahasiswa.prog_studi, mahasiswa.fakultas, mahasiswa.umur, mahasiswa.email))


def main():
    daftar_mahasiswa = DaftarMahasiswa()
    daftar_mahasiswa.tambah_mahasiswa(Mahasiswa(
        "John Doe", "123456789", "Teknik Informatika", "Teknologi Informasi", 20, "john.doe@contoh.com"))
    daftar_mahasiswa.tambah_mahasiswa(Mahasiswa(
        "Jane Doe", "987654321", "Sistem Informasi", "Teknologi Informasi", 21, "jane.doe@contoh.com"))
    daftar_mahasiswa.tampilkan_daftar()

    while True:
        print("Menu:")
        print("1. Tambah Mahasiswa")
        print("2. Ubah Mahasiswa")
        print("3. Hapus Mahasiswa")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nim = input("Masukkan NIM: ")
            prog_studi = input("Masukkan program studi: ")
            fakultas = input("Masukkan fakultas: ")
            umur = int(input("Masukkan umur: "))
            email = input("Masukkan email: ")
            mahasiswa = Mahasiswa(nama, nim, prog_studi, fakultas, umur, email)
            daftar_mahasiswa.tambah_mahasiswa(mahasiswa)
            daftar_mahasiswa.tampilkan_daftar()

        elif pilihan == "2":
            index = int(input("Masukkan indeks mahasiswa yang akan diubah: "))
            mahasiswa = daftar_mahasiswa.list_mahasiswa[index]
            print("Data mahasiswa yang akan diubah:")
            print("{:<20} {:<15} {:<25} {:<20} {:<5} {:<25}".format(
                "Nama", "NIM", "Program Studi", "Fakultas", "Umur", "Email"))
            print("{:<20} {:<15} {:<25} {:<20} {:<5} {:<25}".format(mahasiswa.nama, mahasiswa.nim,
                  mahasiswa.prog_studi, mahasiswa.fakultas, mahasiswa.umur, mahasiswa.email))
            nama = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
            nim = input("Masukkan NIM baru (kosongkan jika tidak diubah): ")
            prog_studi = input(
                "Masukkan program studi baru (kosongkan jika tidak diubah): ")
            fakultas = input(
                "Masukkan fakultas baru (kosongkan jika tidak diubah): ")
            umur = input("Masukkan umur baru (kosongkan jika tidak diubah): ")
            if umur:
                umur = int(umur)
            email = input(
                "Masukkan email baru (kosongkan jika tidak diubah): ")
            if nama or nim or prog_studi or fakultas or umur or email:
                if not nama:
                    nama = mahasiswa.nama
                if not nim:
                    nim = mahasiswa.nim
                if not prog_studi:
                    prog_studi = mahasiswa.prog_studi
                if not fakultas:
                    fakultas = mahasiswa.fakultas
                if not umur:
                    umur = mahasiswa.umur
                if not email:
                    email = mahasiswa.email
                mahasiswa_baru = Mahasiswa(
                    nama, nim, prog_studi, fakultas, umur, email)
                daftar_mahasiswa.ubah_mahasiswa(index, mahasiswa_baru)
                daftar_mahasiswa.tampilkan_daftar()

        elif pilihan == "3":
            index = int(input("Masukkan indeks mahasiswa yang akan dihapus: "))
            daftar_mahasiswa.hapus_mahasiswa(index)
            daftar_mahasiswa.tampilkan_daftar()

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
