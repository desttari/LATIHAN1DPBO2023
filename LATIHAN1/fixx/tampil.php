<!-- PHP berkedok HTML untuk menampilkan data yg tlh diinput ke dalam tabel -->
<!DOCTYPE html>
<html>
<head>
	<title>Data Mahasiswa</title>
</head>
<body>
	<h1>Data Mahasiswa</h1>
	<table border="1">
		<tr>
			<th>NIM</th>
			<th>Nama</th>
			<th>Program Studi</th>
			<th>Fakultas</th>
			<th>Angkatan</th>
			<th>Email</th>
		</tr>
		<?php
        // read data yang telah dimasukan
        //dimasukan ke text karena mysql error tk bisa save ke database
		$file = fopen("data.txt", "r");
        //print isi file
		while (($data = fgetcsv($file)) !== false) {
			echo "<tr>";
			echo "<td>" . $data[0] . "</td>";
			echo "<td>" . $data[1] . "</td>";
			echo "<td>" . $data[2] . "</td>";
			echo "<td>" . $data[3] . "</td>";
			echo "<td>" . $data[4] . "</td>";
			echo "<td>" . $data[5] . "</td>";
			echo "</tr>";
		}
		fclose($file);
		?>
	</table>
	<br>
    <!-- tombol kembali ke menu inputan -->
	<a href="index.html">Kembali</a>
</body>
</html>
