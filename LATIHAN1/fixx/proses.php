<?php
//proses ambil data yg dinput kemudian disimpan ke dalam file.txt
if (isset($_POST['submit'])) {
	$nim = $_POST['nim'];
	$nama = $_POST['nama'];
	$prodi = $_POST['prodi'];
	$fakultas = $_POST['fakultas'];
	$angkatan = $_POST['angkatan'];
	$email = $_POST['email'];
    //semua data yg diinput dimasukan ke variabel data
	$data = [
		'nim' => $nim,
		'nama' => $nama,
		'prodi' => $prodi,
		'fakultas' => $fakultas,
		'angkatan' => $angkatan,
		'email' => $email
	];
    //memasukan data ke file txt
	$file = fopen("data.txt", "a+");
	fputcsv($file, $data);
	fclose($file);

	echo "Data berhasil disimpan!";
}
?>

