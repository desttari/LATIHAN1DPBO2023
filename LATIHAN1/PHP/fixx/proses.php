

<?php
//kelas mahasiswa
class Mahasiswa {
	private $nim;
	private $nama;
	private $prodi;
	private $fakultas;
	private $angkatan;
	private $email;

    //construct
	public function __construct($nim, $nama, $prodi, $fakultas, $angkatan, $email) {
		$this->nim = $nim;
		$this->nama = $nama;
		$this->prodi = $prodi;
		$this->fakultas = $fakultas;
		$this->angkatan = $angkatan;
		$this->email = $email;
	}

    //getter setter
	public function setNim($nim) {
		$this->nim = $nim;
	}

	public function getNim() {
		return $this->nim;
	}

	public function setNama($nama) {
		$this->nama = $nama;
	}

	public function getNama() {
		return $this->nama;
	}

	public function setProdi($prodi) {
		$this->prodi = $prodi;
	}

	public function getProdi() {
		return $this->prodi;
	}

	public function setFakultas($fakultas) {
		$this->fakultas = $fakultas;
	}

	public function getFakultas() {
		return $this->fakultas;
	}

	public function setAngkatan($angkatan) {
		$this->angkatan = $angkatan;
	}

	public function getAngkatan() {
		return $this->angkatan;
	}

	public function setEmail($email) {
		$this->email = $email;
	}

	public function getEmail() {
		return $this->email;
	}
}
//semua data yg diinput dimasukan ke variabel data
$mahasiswa = new Mahasiswa($_POST['nim'], $_POST['nama'], $_POST['prodi'], $_POST['fakultas'], $_POST['angkatan'], $_POST['email']);
//memasukan data ke file txt, dengan append baca tulis file
$file = fopen("data.txt", "a+");
fputcsv($file, [$mahasiswa->getNim(), $mahasiswa->getNama(), $mahasiswa->getProdi(), $mahasiswa->getFakultas(), $mahasiswa->getAngkatan(), $mahasiswa->getEmail()]);
fclose($file);

echo "Data berhasil disimpan!";
?>


