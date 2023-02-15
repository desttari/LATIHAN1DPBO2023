//panggil library
#include <bits/stdc++.h>
#include "Mahasiswa.cpp"
#include <iostream>

int main() {
    // Initialize max mahasiswa 1000 data
    const int MAX = 1000;
    Mahasiswa mhs[MAX];
    //data awal yg ada
    int count = 0;
    
    do {
        //menu portal
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
        
        //iny untuk pilhan menu
        int pilihan;
        //input user untuk menu terpilih
        cin >> pilihan;
        
        if (pilihan == 1) {//menu tambah data
            if (count == MAX) {//jika penuh
                cout << "Data mahasiswa penuh." << endl;
                cout << '\n' << endl;
            } else {//jika tdk penuh input dr user untuk data mahasiswa
                string NIM, nama, jurusan, no_hp, fakultas;
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
                cout << "Masukkan fakultas: ";
                cin.ignore();
                getline(cin, fakultas);
                cout << "Masukkan jurusan: ";
                getline(cin, jurusan);
                cout << '\n' << endl;

                //dimasukkan ke temporary untuk kemudian di masukkan ke array
                Mahasiswa temp;
                temp.setNIM(NIM);
                temp.setNama(nama);
                temp.setJenisKelamin(jenis_kelamin);
                temp.setUmur(umur);
                temp.setNoHP(no_hp);
                temp.setFakultas(fakultas);
                temp.setJurusan(jurusan);
            
            mhs[count] = temp;
            count++; //data bertambah
            
            cout << "Data mahasiswa berhasil ditambahkan." << endl;
            cout << '\n' << endl;
        }
        } else if (pilihan == 2) {//menu edit
            if (count == 0) {//jika data 0
                cout << "Belum ada data mahasiswa." << endl;
                cout << '\n' << endl;
            } else {//jika ada data
                string NIM;
                cout << '\n' << endl;
                //edit berdasarkan NIM
                cout << "Masukkan NIM yang akan diedit: ";
                cin >> NIM;
                
                //cek NIM yg sama dgn yg dicari
                int idx = -1;
                for (int i = 0; i < count; i++) {
                    if (mhs[i].getNIM() == NIM) {
                        idx = i;
                        break;
                    }
                }
                //jika tdk ada yg sama
                if (idx == -1) {
                    cout << '\n' << endl;
                    cout << "Data mahasiswa dengan NIM tersebut tidak ditemukan." << endl;
                    cout << '\n' << endl;
                } else {//jika nim ketemu
                    string nama, jurusan, no_hp, fakultas;
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
                    cout << "Masukkan fakultas: ";
                    cin.ignore();
                    getline(cin, fakultas);
                    cout << "Masukkan jurusan: ";
                    getline(cin, jurusan);
                    cout << '\n' << endl;

                    //disimpan ke array
                    mhs[idx].setNama(nama);
                    mhs[idx].setJenisKelamin(jenis_kelamin);
                    mhs[idx].setUmur(umur);
                    mhs[idx].setNoHP(no_hp);
                    mhs[idx].setFakultas(fakultas);
                    mhs[idx].setJurusan(jurusan);
                    
                    cout << "Data mahasiswa berhasil diubah." << endl;
                    cout << '\n' << endl;
                }
            }
        } else if (pilihan == 3) {//menu hapus berdasar nim
            if (count == 0) {
                cout << '\n' << endl;
                cout << "Belum ada data mahasiswa." << endl;
                cout << '\n' << endl;
            } else {
                string NIM;
                cout << '\n' << endl;
                cout << "Masukkan NIM yang akan dihapus: ";
                cin >> NIM;
                
                //cari sesuai nim
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
        } else if (pilihan == 4) {//menu menampilkan data mahasiswa dengan list ke bawah
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
                    cout << "Fakultas      : " << mhs[i].getFakultas() << endl;
                    cout << "Jurusan       : " << mhs[i].getJurusan() << endl;
                    cout << '\n' << endl;
                }
            }
        } else if (pilihan == 5) {//menu keluar program
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
    } while (true);//selama belum keluar program akan terus menampilkan menu

    return 0;
}
