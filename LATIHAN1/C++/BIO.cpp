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

int main() {
    const int MAX = 1000;
    Mahasiswa mhs[MAX];
    int count = 0;
    
    do {
        cout << '\n' << endl;
        cout << "------------------------------------------------------------------------" << endl;
        cout << "------------------------------------------------------------------------" << endl;
        cout << "---------------SELAMAT DATANG DI PORTAL BIODATA MAHASISWA---------------" << endl;
        cout << "------------------------------------------------------------------------" << endl;
        cout << "------------------------------------------------------------------------" << endl;
        cout << '\n' << endl;
        cout << "--------------------SILAHKAN PILIH MENU DI BAWAH INI--------------------" << endl;
        cout << '\n' << endl;
        cout << "Menu:" << endl;
        cout << "1. Tambah Data" << endl;
        cout << "2. Edit Data" << endl;
        cout << "3. Hapus Data" << endl;
        cout << "4. Tampilkan Data" << endl;
        cout << "5. Keluar" << endl;
        cout << "Pilihan: ";
        
        int pilihan;
        cin >> pilihan;
        
        if (pilihan == 1) {
            if (count == MAX) {
                cout << "Data mahasiswa penuh." << endl;
                cout << '\n' << endl;
            } else {
                string NIM, nama, jurusan, no_hp, alamat;
                int umur;
                char jenis_kelamin;

                cout << '\n' << endl;
                cout << "Masukkan NIM: ";
                cin >> NIM;
                cout << "Masukkan nama: ";
                cin.ignore();
                getline(cin, nama);
                cout << "Masukkan jenis kelamin (L/P): ";
                cin >> jenis_kelamin;
                cout << "Masukkan umur: ";
                cin >> umur;
                cout << "Masukkan nomor handphone: ";
                cin >> no_hp;
                cout << "Masukkan alamat: ";
                cin.ignore();
                getline(cin, alamat);
                cout << "Masukkan jurusan: ";
                getline(cin, jurusan);
                cout << '\n' << endl;

                Mahasiswa temp;
                temp.setNIM(NIM);
                temp.setNama(nama);
                temp.setJenisKelamin(jenis_kelamin);
                temp.setUmur(umur);
                temp.setNoHP(no_hp);
                temp.setAlamat(alamat);
                temp.setJurusan(jurusan);
            
            mhs[count] = temp;
            count++;
            
            cout << "Data mahasiswa berhasil ditambahkan." << endl;
            cout << '\n' << endl;
        }
        } else if (pilihan == 2) {
            if (count == 0) {
                cout << "Belum ada data mahasiswa." << endl;
                cout << '\n' << endl;
            } else {
                string NIM;
                cout << '\n' << endl;
                cout << "Masukkan NIM yang akan diedit: ";
                cin >> NIM;
                
                int idx = -1;
                for (int i = 0; i < count; i++) {
                    if (mhs[i].getNIM() == NIM) {
                        idx = i;
                        break;
                    }
                }
                
                if (idx == -1) {
                    cout << '\n' << endl;
                    cout << "Data mahasiswa dengan NIM tersebut tidak ditemukan." << endl;
                    cout << '\n' << endl;
                } else {
                    string nama, jurusan, no_hp, alamat;
                    int umur;
                    char jenis_kelamin;

                    cout << '\n' << endl;
                    cout << "Masukkan nama: ";
                    cin.ignore();
                    getline(cin, nama);
                    cout << "Masukkan jenis kelamin (L/P): ";
                    cin >> jenis_kelamin;
                    cout << "Masukkan umur: ";
                    cin >> umur;
                    cout << "Masukkan nomor handphone: ";
                    cin >> no_hp;
                    cout << "Masukkan alamat: ";
                    cin.ignore();
                    getline(cin, alamat);
                    cout << "Masukkan jurusan: ";
                    getline(cin, jurusan);
                    cout << '\n' << endl;

                    mhs[idx].setNama(nama);
                    mhs[idx].setJenisKelamin(jenis_kelamin);
                    mhs[idx].setUmur(umur);
                    mhs[idx].setNoHP(no_hp);
                    mhs[idx].setAlamat(alamat);
                    mhs[idx].setJurusan(jurusan);
                    
                    cout << "Data mahasiswa berhasil diubah." << endl;
                    cout << '\n' << endl;
                }
            }
        } else if (pilihan == 3) {
            if (count == 0) {
                cout << '\n' << endl;
                cout << "Belum ada data mahasiswa." << endl;
                cout << '\n' << endl;
            } else {
                string NIM;
                cout << '\n' << endl;
                cout << "Masukkan NIM yang akan dihapus: ";
                cin >> NIM;
                
                int idx = -1;
                for (int i = 0; i < count; i++) {
                    if (mhs[i].getNIM() == NIM) {
                        idx = i;
                        break;
                    }
                }
                
                if (idx == -1) {
                    cout << '\n' << endl;
                    cout << "Data mahasiswa dengan NIM tersebut tidak ditemukan." << endl;
                    cout << '\n' << endl;
                } else {
                    for (int i = idx; i < count - 1; i++) {
                        mhs[i] = mhs[i+1];
                    }
                    count--;
                    
                    cout << "Data mahasiswa berhasil dihapus." << endl;
                    cout << '\n' << endl;
                }
            }
        } else if (pilihan == 4) {
            if (count == 0) {
                cout << '\n' << endl;
                cout << "Belum ada data mahasiswa." << endl;
                cout << '\n' << endl;
            } else {
                cout << '\n' << endl;
                cout << "Data mahasiswa:" << endl;
                for (int i = 0; i < count; i++) {
                    cout << "NIM           : " << mhs[i].getNIM() << endl;
                    cout << "Nama          : " << mhs[i].getNama() << endl;
                    cout << "Jenis Kelamin : " << mhs[i].getJenisKelamin() << endl;
                    cout << "Umur          : " << mhs[i].getUmur() << endl;
                    cout << "Nomor HP      : " << mhs[i].getNoHP() << endl;
                    cout << "Alamat        : " << mhs[i].getAlamat() << endl;
                    cout << "Jurusan       : " << mhs[i].getJurusan() << endl;
                    cout << '\n' << endl;
                }
            }
        } else if (pilihan == 5) {
            cout << "------------------------------------------------------------------------" << endl;
            cout << "------------------------------------------------------------------------" << endl;
            cout << "---------------------------HAVE A NICE DAY :D---------------------------" << endl;
            cout << "------------------------------------------------------------------------" << endl;
            cout << "---------------------------------------------------------------------DLS" << endl;
            cout << '\n' << endl;
            break;
        } else {
            cout << '\n' << endl;
            cout << "Mohon pilih Menu yang tersedia" << endl;
            cout << '\n' << endl;
        }
    } while (true);

    return 0;
}
