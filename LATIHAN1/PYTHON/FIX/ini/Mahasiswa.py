class Mahasiswa:  # kelas mahasiswa
    # private atribut, constructor
    def __init__(self):
        self.NIM = ""
        self.nama = ""
        self.umur = 0
        self.jurusan = ""
        self.jenis_kelamin = "-"
        self.no_hp = ""
        self.alamat = ""

    # public setter dan getter
    def setNIM(self, NIM):
        self.NIM = NIM

    def getNIM(self):
        return self.NIM

    def setNama(self, nama):
        self.nama = nama

    def getNama(self):
        return self.nama

    def setUmur(self, umur):
        self.umur = umur

    def getUmur(self):
        return self.umur

    def setJurusan(self, jurusan):
        self.jurusan = jurusan

    def getJurusan(self):
        return self.jurusan

    def setJenisKelamin(self, jenis_kelamin):
        self.jenis_kelamin = jenis_kelamin

    def getJenisKelamin(self):
        return self.jenis_kelamin

    def setNoHP(self, no_hp):
        self.no_hp = no_hp

    def getNoHP(self):
        return self.no_hp

    def setAlamat(self, alamat):
        self.alamat = alamat

    def getAlamat(self):
        return self.alamat

    # destructor
    def __del__(self):
        pass
