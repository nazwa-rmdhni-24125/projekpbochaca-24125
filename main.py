from sistem import SistemMahasiswa

def main():
    sistem = SistemMahasiswa()

    sistem.tambah_mahasiswa("230401", "Andi", "Informatika")
    sistem.tambah_mahasiswa("230402", "Budi", "Informatika")
    sistem.tambah_mahasiswa("230403", "Citra", "Informatika")

    sistem.tampilkan_semua()

if __name__ == "__main__":
    main()
