from Mahasiswa import Mahasiswa


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
