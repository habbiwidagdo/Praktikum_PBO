class Kalkulator:
    def __init__(self, x):
        self.x = x  # Gunakan atribut private (_x)

    def __add__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.x + other.x)
        raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.x - other.x)
        raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.x * other.x)
        raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Kalkulator):
            if other.x == 0:
                raise ZeroDivisionError("Tidak bisa membagi dengan nol!")
            return Kalkulator(self.x / other.x)
        raise TypeError("Unsupported operand type for /")

    def __pow__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.x ** other.x)
        raise TypeError("Unsupported operand type for **")

    def __str__(self):
        return f"Hasil: {self.x}"

while True:
    angka1 = float(input("Input nilai pertama: "))  # Konversi ke float
    operasi = input("Pilih operasi (+, -, *, /, ^): ")
    angka2 = float(input("Input nilai kedua: "))  # Konversi ke float

    hitung1 = Kalkulator(angka1)
    hitung2 = Kalkulator(angka2)

    if operasi == '+':
        hasil = hitung1 + hitung2
    elif operasi == '-':
        hasil = hitung1 - hitung2
    elif operasi == '*':
        hasil = hitung1 * hitung2
    elif operasi == '/':
        hasil = hitung1 / hitung2
    elif operasi == '^':
        hasil = hitung1 ** hitung2
    else:
        raise ValueError("Operasi tidak valid! Gunakan +, -, *, /, atau ^.")
    print(hasil)
    check = input("Anda ingin menghitung lagi?(y/n): ")
    if check == 'n':
        break