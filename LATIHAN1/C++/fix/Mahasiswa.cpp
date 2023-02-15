#include <iostream>
#include <string>
using namespace std;

class Mahasiswa {
    private:
        string NIM;
        string nama;
        int umur;
        string jurusan;
        char jenis_kelamin;
        string no_hp;
        string alamat;
        
    public:
        Mahasiswa() {
            NIM = "";
            nama = "";
            umur = 0;
            jurusan = "";
            jenis_kelamin = '-';
            no_hp = "";
            alamat = "";
        }
        
        void setNIM(string NIM) {
            this->NIM = NIM;
        }
        
        string getNIM() {
            return NIM;
        }
        
        void setNama(string nama) {
            this->nama = nama;
        }
        
        string getNama() {
            return nama;
        }
        
        void setUmur(int umur) {
            this->umur = umur;
        }
        
        int getUmur() {
            return umur;
        }
        
        void setJurusan(string jurusan) {
            this->jurusan = jurusan;
        }
        
        string getJurusan() {
            return jurusan;
        }

        void setJenisKelamin(char jenis_kelamin) {
            this->jenis_kelamin = jenis_kelamin;
        }

        char getJenisKelamin() {
            return jenis_kelamin;
        }

        void setNoHP(string no_hp) {
            this->no_hp = no_hp;
        }

        string getNoHP() {
            return no_hp;
        }

        void setAlamat(string alamat) {
            this->alamat = alamat;
        }

        string getAlamat() {
            return alamat;
        }

        ~Mahasiswa(){

        }
};