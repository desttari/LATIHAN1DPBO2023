// import scanner
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    // batas banyak data
    final int MAX = 1000;
    Mahasiswa[] mhs = new Mahasiswa[MAX];
    // tanda data kosong
    int count = 0;

    // wadah input user
    Scanner input = new Scanner(System.in);

    do {
      // menu portal
      System.out.println(
          "\n------------------------------------------------------------------------");
      System.out.println(
          "------------------------------------------------------------------------");
      System.out.println(
          "---------------SELAMAT DATANG DI PORTAL BIODATA MAHASISWA---------------");
      System.out.println(
          "------------------------------------------------------------------------");
      System.out.println(
          "------------------------------------------------------------------------\n");
      System.out.println(
          "--------------------SILAHKAN PILIH MENU DI BAWAH INI--------------------\n");
      System.out.println("Menu:");
      System.out.println("1. Tambah Data");
      System.out.println("2. Edit Data");
      System.out.println("3. Hapus Data");
      System.out.println("4. Tampilkan Data");
      System.out.println("5. Keluar");
      System.out.print("Pilihan: ");

      // piliham menu user
      int pilihan = input.nextInt();

      if (pilihan == 1) { // menu tambah data
        if (count == MAX) {
          System.out.println("Data mahasiswa penuh.\n");
        } else {
          String NIM, nama, jurusan, no_hp, fakultas;
          int umur;
          char jenis_kelamin;

          System.out.print("\nMasukkan NIM: ");
          NIM = input.next();
          input.nextLine(); // consume the newline character
          System.out.print("Masukkan nama: ");
          nama = input.nextLine();
          System.out.print("Masukkan jenis kelamin (L/P): ");
          jenis_kelamin = input.next().charAt(0);
          System.out.print("Masukkan umur: ");
          umur = input.nextInt();
          System.out.print("Masukkan nomor handphone: ");
          no_hp = input.next();
          input.nextLine(); // consume the newline character
          System.out.print("Masukkan fakultas: ");
          fakultas = input.nextLine();
          System.out.print("Masukkan jurusan: ");
          jurusan = input.nextLine();
          System.out.println();

          Mahasiswa temp = new Mahasiswa();
          temp.setNIM(NIM);
          temp.setNama(nama);
          temp.setJenisKelamin(jenis_kelamin);
          temp.setUmur(umur);
          temp.setNoHP(no_hp);
          temp.setFakultas(fakultas);
          temp.setJurusan(jurusan);

          // masukan data dari inputan user
          mhs[count] = temp;
          count++;

          System.out.println("Data mahasiswa berhasil ditambahkan.\n");
        }
      } else if (pilihan == 2) { // menu edit data berdasar nim
        if (count == 0) {
          System.out.println("Belum ada data mahasiswa.\n");
        } else {
          String NIM;
          System.out.println("\nMasukkan NIM yang akan diedit: ");
          NIM = input.nextLine();

          // cari nim yg sama
          int idx = -1;
          for (int i = 0; i < count; i++) {
            if (mhs[i].getNIM().equals(NIM)) {
              idx = i;
              break;
            }
          }

          if (idx == -1) {
            System.out.println(
                "\nData mahasiswa dengan NIM tersebut tidak ditemukan.\n");
          } else {
            String nama, jurusan, no_hp, fakultas;
            int umur;
            char jenis_kelamin;

            // masukan data baru
            System.out.println("\nMasukkan nama: ");
            input.nextLine();
            nama = input.nextLine();
            System.out.println("Masukkan jenis kelamin (L/P): ");
            jenis_kelamin = input.next().charAt(0);
            System.out.println("Masukkan umur: ");
            umur = input.nextInt();
            System.out.println("Masukkan nomor handphone: ");
            no_hp = input.next();
            System.out.println("Masukkan fakultas: ");
            input.nextLine();
            fakultas = input.nextLine();
            System.out.println("Masukkan jurusan: ");
            jurusan = input.nextLine();
            System.out.println();

            mhs[idx].setNama(nama);
            mhs[idx].setJenisKelamin(jenis_kelamin);
            mhs[idx].setUmur(umur);
            mhs[idx].setNoHP(no_hp);
            mhs[idx].setFakultas(fakultas);
            mhs[idx].setJurusan(jurusan);

            System.out.println("Data mahasiswa berhasil diubah.\n");
          }
        }
      } else if (pilihan == 3) { // menu hapus data berdasar nim
        if (count == 0) {
          System.out.println("\nBelum ada data mahasiswa.\n");
        } else {
          String NIM;
          System.out.println("\nMasukkan NIM yang akan dihapus: ");
          Scanner scanner = new Scanner(System.in);
          NIM = scanner.next();

          // cari nim yg sama
          int idx = -1;
          for (int i = 0; i < count; i++) {
            if (mhs[i].getNIM().equals(NIM)) {
              idx = i;
              break;
            }
          }

          if (idx == -1) {
            System.out.println(
                "\nData mahasiswa dengan NIM tersebut tidak ditemukan.\n");
          } else {
            for (int i = idx; i < count - 1; i++) {
              mhs[i] = mhs[i + 1];
            }
            count--;

            System.out.println("Data mahasiswa berhasil dihapus.\n");
          }
        }
      } else if (pilihan == 4) { // menu menampilkan data
        if (count == 0) {
          System.out.println("\nBelum ada data mahasiswa.\n");
        } else {
          System.out.println("\nData mahasiswa:\n");
          for (int i = 0; i < count; i++) {
            System.out.println("NIM           : " + mhs[i].getNIM());
            System.out.println("Nama          : " + mhs[i].getNama());
            System.out.println("Jenis Kelamin : " + mhs[i].getJenisKelamin());
            System.out.println("Umur          : " + mhs[i].getUmur());
            System.out.println("Nomor HP      : " + mhs[i].getNoHP());
            System.out.println("Fakultas      : " + mhs[i].getFakultas());
            System.out.println("Jurusan       : " + mhs[i].getJurusan());
            System.out.println("\n");
          }
        }
      } else if (pilihan == 5) { // menu keluar program
        System.out.println(
            "------------------------------------------------------------------------");
        System.out.println(
            "------------------------------------------------------------------------");
        System.out.println(
            "---------------------------HAVE A NICE DAY :D---------------------------");
        System.out.println(
            "------------------------------------------------------------------------");
        System.out.println(
            "---------------------------------------------------------------------DLS");
        System.out.println('\n');
        break;
      } else {
        System.out.println('\n');
        System.out.println("Mohon pilih Menu yang tersedia");
        System.out.println('\n');
      }

    } while (true); // terus looping sampai menu 5 dipilih
  }
}
