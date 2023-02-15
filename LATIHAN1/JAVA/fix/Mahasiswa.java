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
