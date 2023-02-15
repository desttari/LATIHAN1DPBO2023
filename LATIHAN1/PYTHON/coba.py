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

    def ubah_mahasiswa(self, nim, mahasiswa):
        for i, mhs in enumerate(self.list_mahasiswa):
            if mhs.nim == nim:
                self.list_mahasiswa[i] = mahasiswa
                print("Data mahasiswa dengan NIM {} berhasil diubah.".format(nim))
                return
        print("Tidak ditemukan mahasiswa dengan NIM {}.".format(nim))

    def hapus_mahasiswa(self, nim):
        for i, mhs in enumerate(self.list_mahasiswa):
            if mhs.nim == nim:
                self.list_mahasiswa.pop(i)
                print("Data mahasiswa dengan NIM {} berhasil dihapus.".format(nim))
                return
        print("Tidak ditemukan mahasiswa dengan NIM {}.".format(nim))

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
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            prog_studi = input("Masukkan program studi mahasiswa: ")
            fakultas = input("Masukkan fakultas mahasiswa: ")
            umur = input("Masukkan umur mahasiswa: ")
            email = input("Masukkan email mahasiswa: ")
            daftar_mahasiswa.tambah_mahasiswa(
                Mahasiswa(nama, nim, prog_studi, fakultas, umur, email))
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa: ")
            nama = input("Masukkan nama mahasiswa: ")
            prog_studi = input("Masukkan program studi mahasiswa: ")
            fakultas = input("Masukkan fakultas mahasiswa: ")
            umur = input("Masukkan umur mahasiswa: ")
            email = input("Masukkan email mahasiswa: ")
            daftar_mahasiswa.ubah_mahasiswa(
                nim, Mahasiswa(nama, nim, prog_studi, fakultas, umur, email))

        elif pilihan == "3":
            index = int(input("Masukkan NIM mahasiswa: "))
            daftar_mahasiswa.hapus_mahasiswa(index)

        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
