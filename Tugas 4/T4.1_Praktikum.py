class ZeroError(Exception):
    pass
class MinusError(Exception):
    pass
def HitungAkarKuadrat(s):
    if s < 0:
        raise MinusError("Input tidak valid. Harap masukkan angka positif.")
    elif s == 0:
        raise ZeroError("Akar kuadrat dari nol tidak diperbolehkan.")
    i = float(1)
    while i**2 <= s:
        cek = i**2
        if cek == s:
            return i
        i += 1
try:
    x = int(input("Masukkan angka: "))
    Hitung = HitungAkarKuadrat(x)
    print(f"Akar kuadrat dari {x} adalah {Hitung}")
except ValueError as e:
    print("Input tidak valid. Harap masukkan angka yang valid.")
except MinusError as e:
    print(e)
except ZeroError as e:
    print(f"Error: {e}")