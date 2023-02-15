import java.util.Scanner;

public class Main {
  private static final int MAX_STUDENTS = 1000;

  public static void main(String[] args) {
    Mahasiswa[] mhs = new Mahasiswa[MAX_STUDENTS];
    int count = 0;

    Scanner input = new Scanner(System.in);

    while (true) {
      printMenu();
      int choice = readIntInput(input, "Pilihan: ");

      switch (choice) {
      case 1:
        if (count == MAX_STUDENTS) {
          System.out.println("Data mahasiswa penuh.");
        } else {
          Mahasiswa newStudent = readStudentInput(input);
          mhs[count] = newStudent;
          count++;
          System.out.println("Data mahasiswa berhasil ditambahkan.");
        }
        break;

      case 2:
        if (count == 0) {
          System.out.println("Belum ada data mahasiswa.");
        } else {
          String nim =
              readStringInput(input, "Masukkan NIM yang akan diedit: ");
          int index = findStudentIndex(mhs, count, nim);

          if (index == -1) {
            System.out.println(
                "Data mahasiswa dengan NIM tersebut tidak ditemukan.");
          } else {
            Mahasiswa editedStudent = readStudentInput(input);
            mhs[index] = editedStudent;
            System.out.println("Data mahasiswa berhasil diubah.");
          }
        }
        break;

      case 3:
        if (count == 0) {
          System.out.println("Belum ada data mahasiswa.");
        } else {
          String nim =
              readStringInput(input, "Masukkan NIM yang akan dihapus: ");
          int index = findStudentIndex(mhs, count, nim);

          if (index == -1) {
            System.out.println(
                "Data mahasiswa dengan NIM tersebut tidak ditemukan.");
          } else {
            for (int i = index; i < count - 1; i++) {
              mhs[i] = mhs[i + 1];
            }
            count--;
            System.out.println("Data mahasiswa berhasil dihapus.");
          }
        }
        break;

      case 4:
        if (count == 0) {
          System.out.println("Belum ada data mahasiswa.");
        } else {
          printStudentList(mhs, count);
        }
        break;

      case 5:
        System.out.println("Terima kasih telah menggunakan program ini.");
        return;

      default:
        System.out.println("Pilihan tidak valid.");
      }
    }
  }

  private static void printMenu() {
    System.out.println("=====================================");
    System.out.println("==   PORTAL BIODATA MAHASISWA      ==");
    System.out.println("=====================================");
    System.out.println("1. Tambah Data");
    System.out.println("2. Edit Data");
    System.out.println("3. Hapus Data");
    System.out.println("4. Tampilkan Data");
    System.out.println("5. Keluar");
  }

  private static Mahasiswa readStudentInput(Scanner input) {
    String nim = readStringInput(input, "Masukkan NIM: ");
    String name = readStringInput(input, "Masukkan nama: ");
    char gender = readCharInput(input, "Masukkan jenis kelamin (L/P): ");
    int age = readIntInput(input, "Masukkan umur: ");
    String phone = readStringInput(input, "Masukkan nomor handphone: ");
    String address = readStringInput(input, "Masukkan alamat: ");
    return new Mahasiswa(nim, name, gender, age, phone, address);
  }

  private static int readIntInput(Scanner input, String message) {
    System.out.print(message);
    while (!input.hasNextInt()) {
      input.next();
      System.out.print("Input tidak valid. " + message);
    }
    return input.nextInt();
  }

  private static String readStringInput(Scanner input, String message) {
    System.out.print(message);
    return input.next();
  }
}
