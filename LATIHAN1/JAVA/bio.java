import java.util.Scanner;

public class Mahasiswa {
  private String NIM;
  private String nama;
  private int umur;
  private String jurusan;
  private char jenis_kelamin;
  private String no_hp;
  private String alamat;

  public Mahasiswa() {
    NIM = "";
    nama = "";
    umur = 0;
    jurusan = "";
    jenis_kelamin = '-';
    no_hp = "";
    alamat = "";
  }

  public void setNIM(String NIM) { this.NIM = NIM; }

  public String getNIM() { return NIM; }

  public void setNama(String nama) { this.nama = nama; }

  public String getNama() { return nama; }

  public void setUmur(int umur) { this.umur = umur; }

  public int getUmur() { return umur; }

  public void setJurusan(String jurusan) { this.jurusan = jurusan; }

  public String getJurusan() { return jurusan; }

  public void setJenisKelamin(char jenis_kelamin) {
    this.jenis_kelamin = jenis_kelamin;
  }

  public char getJenisKelamin() { return jenis_kelamin; }

  public void setNoHP(String no_hp) { this.no_hp = no_hp; }

  public String getNoHP() { return no_hp; }

  public void setAlamat(String alamat) { this.alamat = alamat; }

  public String getAlamat() { return alamat; }
}

public class Main {
  public static void main(String[] args) {
    final int MAX = 1000;
    Mahasiswa[] mhs = new Mahasiswa[MAX];
    int count = 0;

    Scanner sc = new Scanner(System.in);

    do {
      System.out.println("\n");
      System.out.println(
          "------------------------------------------------------------------------");
      System.out.println(
          "------------------------------------------------------------------------");
      System.out.println(
          "---------------SELAMAT DATANG DI PORTAL BIODATA MAHASISWA---------------");
      System.out.println(
          "------------------------------------------------------------------------");
      System.out.println(
          "------------------------------------------------------------------------");
      System.out.println("\n");
      System.out.println(
          "--------------------SILAHKAN PILIH MENU DI BAWAH INI--------------------");
      System.out.println("\n");
      System.out.println("Menu:");
      System.out.println("1. Tambah Data");
      System.out.println("2. Edit Data");
      System.out.println("3. Hapus Data");
      System.out.println("4. Tampilkan Data");
      System.out.println("5. Keluar");
      System.out.print("Pilihan: ");

      int pilihan = sc.nextInt();

      if (pilihan == 1) {
        if (count == MAX) {
          System.out.println("Data mahasiswa penuh.");
          System.out.println("\n");
        } else {
          String NIM, nama, jurusan, no_hp, alamat;
          int umur;
          char jenis_kelamin;

          System.out.println("\n");
          System.out.print("Masukkan NIM: ");
          NIM = sc.next();
          sc.nextLine();

          System.out.print("Masukkan nama: ");
          nama = sc.nextLine();

          System.out.print("Masukkan jenis kelamin (L/P): ");
          jenis_kelamin = sc.next().charAt(0);

          System.out.print("Masukkan umur: ");
          umur = sc.nextInt();

          System.out.print("Masukkan nomor HP: ");
          no_hp = sc.next();

          System.out.print("Masukkan alamat: ");
          alamat = sc.next();

          mhs[count] = new Mahasiswa();
          mhs[count].setNIM(NIM);
          mhs[count].setNama(nama);
          mhs[count].setJenisKelamin(jenis_kelamin);
          mhs[count].setUmur(umur);
          mhs[count].setNoHP(no_hp);
          mhs[count].setAlamat(alamat);

          System.out.println("\nData berhasil ditambahkan.\n");
          count++;
        }
      } else if (pilihan == 2) {
        if (count == 0) {
          System.out.println("Data mahasiswa kosong.");
          System.out.println("\n");
        } else {
          String NIM, nama, jurusan, no_hp, alamat;
          int umur;
          char jenis_kelamin;

          System.out.print("Masukkan NIM mahasiswa yang akan diedit: ");
          NIM = sc.next();

          int idx = -1;

          for (int i = 0; i < count; i++) {
            if (mhs[i].getNIM().equals(NIM)) {
              idx = i;
              break;
            }
          }

          if (idx == -1) {
            System.out.println("NIM tidak ditemukan.");
            System.out.println("\n");
          } else {
            System.out.println("Data mahasiswa yang akan diedit:");
            System.out.println("NIM          : " + mhs[idx].getNIM());
            System.out.println("Nama         : " + mhs[idx].getNama());
            System.out.println("Jenis Kelamin: " + mhs[idx].getJenisKelamin());
            System.out.println("Umur         : " + mhs[idx].getUmur());
            System.out.println("Jurusan      : " + mhs[idx].getJurusan());
            System.out.println("No. HP       : " + mhs[idx].getNoHP());
            System.out.println("Alamat       : " + mhs[idx].getAlamat());

            System.out.println("\nMasukkan data baru:");
            System.out.print("Nama baru: ");
            nama = sc.next();
            mhs[idx].setNama(nama);

            System.out.print("Jenis kelamin baru (L/P): ");
            jenis_kelamin = sc.next().charAt(0);
            mhs[idx].setJenisKelamin(jenis_kelamin);

            System.out.print("Umur baru: ");
            umur = sc.nextInt();
            mhs[idx].setUmur(umur);

            System.out.print("Jurusan baru: ");
            jurusan = sc.next();
            mhs[idx].setJurusan(jurusan);

            System.out.print("No. HP baru: ");
            no_hp = sc.next();
            mhs[idx].setNoHP(no_hp);

            System.out.print("Alamat baru: ");
            alamat = sc.next();
            mhs[idx].setAlamat(alamat);

            System.out.println("\nData berhasil diubah.\n");
          }
        }
      } else if (pilihan == 3) {
        if (count == 0) {
          System.out.println("Data mahasiswa kosong.");
          System.out.println("\n");
        } else {
          String NIM;

          System.out.print("Masukkan NIM mahasiswa yang akan dihapus: ");
          NIM = sc.next();

          int idx = -1;

          for (int i = 0; i < count; i++) {
            if (mhs[i].getNIM().equals(NIM)) {
              idx = i;
              break;
            }
          }

          if (idx == -1) {
                        System.out.println("NIM tidak
