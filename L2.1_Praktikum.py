class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        print(f"Jenis           : {self.jenis}")
        print(f"Kecepatan Max   : {self.kecepatan_maksimum} km/jam\n")

    def bergerak(self):
        print(f"{self.jenis} sedang bergerak\n")


class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        print(f"Jenis          : {self.jenis}")
        print(f"Kecepatan Max  : {self.kecepatan_maksimum} km/jam")
        print(f"Merk           : {self.merk}")
        print(f"Jumlah Pintu   : {self.jumlah_pintu}\n")

    def bunyikan_klakson(self):
        return f"{self.merk} bunyi klaksonnya: 'tin tin!'\n"


class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga

    def get_tenaga_kuda(self):
        return self.__tenaga_kuda

    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda = value

    def get_harga(self):
        return self.__harga

    def set_harga(self, value):
        self.__harga = value

    def info_mobil_sport(self):
        print(f"Jenis         : {self.jenis}")
        print(f"Kecepatan Max : {self.kecepatan_maksimum} km/jam")
        print(f"Merk          : {self.merk}")
        print(f"Jumlah Pintu  : {self.jumlah_pintu}")
        print(f"HP            : {self.__tenaga_kuda} HP")
        print(f"Harga         : Rp{self.__harga:,}\n")

    def mode_balap(self):
        return f"Mobil {self.merk} dalam mode balap!\n"


# Membuat objek dan menampilkan informasinya
kendaraan1 = Kendaraan("Motor", 120)
kendaraan1.info_kendaraan()
kendaraan1.bergerak()

mobil1 = Mobil("Mobil", 200, "Toyota", 4)
mobil1.info_mobil()
print(mobil1.bunyikan_klakson())

mobil_sport1 = MobilSport("Mobil Sport", 350, "Ferrari", 2, 700, 5000000000)
mobil_sport1.info_mobil_sport()
mobil_sport1.set_tenaga_kuda(550)
mobil_sport1.set_harga(3000000000)
mobil_sport1.info_mobil_sport()
print(mobil_sport1.mode_balap())