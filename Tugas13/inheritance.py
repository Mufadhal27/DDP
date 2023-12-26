class Hewan:
    def __init__(self, nama, makanan, habitat, reproduksi):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.reproduksi = reproduksi

class Badak(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama, "Tumbuhan", habitat, "Vivipar")
        self.ukuran_cula = 0

    def tumbuh_cula(self, ukuran):
        self.ukuran_cula += ukuran
        print(f"Ukuran cula {self.nama} sekarang {self.ukuran_cula} inci.")

class Ikan(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama, "Plankton", habitat, "Ovipar")
        self.jumlah_seret = 0

    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class Ular(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama, "Hewan kecil", habitat, "Ovipar")
        self.panjang = 0

    def tumbuh_panjang(self, ukuran):
        self.panjang += ukuran
        print(f"Panjang {self.nama} sekarang {self.panjang} inci.")


badak = Badak("Badak Jawa", "Darat")
badak.tumbuh_cula(5)

ikan = Ikan("Ikan Koi", "Air Tawar")
ikan.berenang()

ular = Ular("Ular Sanca", "Tanah")
ular.tumbuh_panjang(10)