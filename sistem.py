from mahasiswa import Mahasiswa

class SistemMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, nim, nama, jurusan):
        mahasiswa = Mahasiswa(nim, nama, jurusan)
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_semua(self):
        print("=== Data Mahasiswa ===")
        for mhs in self.daftar_mahasiswa:
            print(mhs.tampilkan_data())
