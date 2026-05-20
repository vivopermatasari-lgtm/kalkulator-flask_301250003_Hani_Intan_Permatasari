import math

def hitung_aritmatika(data):
    operasi = data.get('operasi')
    hasil = {}

    try:
        a = float(data.get('angka1', 0))
        b = float(data.get('angka2', 0)) if data.get('angka2') else None

        if operasi == 'tambah':
            nilai = a + b
            hasil['nilai'] = nilai
            hasil['rumus'] = f"{a} + {b} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: angka pertama = {a}, angka kedua = {b}",
                f"Gunakan operasi penjumlahan: {a} + {b}",
                f"Hasil = {nilai}"
            ]

        elif operasi == 'kurang':
            nilai = a - b
            hasil['nilai'] = nilai
            hasil['rumus'] = f"{a} - {b} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: angka pertama = {a}, angka kedua = {b}",
                f"Gunakan operasi pengurangan: {a} - {b}",
                f"Hasil = {nilai}"
            ]

        elif operasi == 'kali':
            nilai = a * b
            hasil['nilai'] = nilai
            hasil['rumus'] = f"{a} × {b} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: angka pertama = {a}, angka kedua = {b}",
                f"Gunakan operasi perkalian: {a} × {b}",
                f"Hasil = {nilai}"
            ]

        elif operasi == 'bagi':
            if b == 0:
                hasil['error'] = "Tidak bisa membagi dengan angka 0!"
            else:
                nilai = a / b
                hasil['nilai'] = nilai
                hasil['rumus'] = f"{a} ÷ {b} = {nilai}"
                hasil['langkah'] = [
                    f"Diketahui: angka pertama = {a}, angka kedua = {b}",
                    f"Pastikan pembagi tidak nol: {b} ≠ 0 ✓",
                    f"Gunakan operasi pembagian: {a} ÷ {b}",
                    f"Hasil = {nilai}"
                ]

        elif operasi == 'pangkat':
            nilai = a ** b
            hasil['nilai'] = nilai
            hasil['rumus'] = f"{a}^{b} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: basis = {a}, eksponen = {b}",
                f"Artinya: {a} dikali sebanyak {int(b)} kali",
                f"Gunakan operasi pangkat: {a}^{b}",
                f"Hasil = {nilai}"
            ]

        elif operasi == 'akar':
            if a < 0:
                hasil['error'] = "Tidak bisa menghitung akar dari bilangan negatif!"
            else:
                nilai = math.sqrt(a)
                hasil['nilai'] = round(nilai, 6)
                hasil['rumus'] = f"√{a} = {round(nilai, 6)}"
                hasil['langkah'] = [
                    f"Diketahui: angka = {a}",
                    f"Cari bilangan yang jika dikuadratkan menghasilkan {a}",
                    f"√{a} = {round(nilai, 6)}",
                    f"Hasil = {round(nilai, 6)}"
                ]

        elif operasi == 'modulus':
            if b == 0:
                hasil['error'] = "Tidak bisa modulus dengan angka 0!"
            else:
                nilai = a % b
                hasil['nilai'] = nilai
                hasil['rumus'] = f"{a} mod {b} = {nilai}"
                hasil['langkah'] = [
                    f"Diketahui: angka = {a}, pembagi = {b}",
                    f"Bagi {a} dengan {b}: hasil bagi = {int(a // b)}",
                    f"Sisa pembagian = {a} - ({int(a // b)} × {b})",
                    f"Hasil = {nilai}"
                ]

        elif operasi == 'floor':
            if b == 0:
                hasil['error'] = "Tidak bisa floor division dengan angka 0!"
            else:
                nilai = a // b
                hasil['nilai'] = nilai
                hasil['rumus'] = f"{a} // {b} = {nilai}"
                hasil['langkah'] = [
                    f"Diketahui: angka pertama = {a}, angka kedua = {b}",
                    f"Bagi {a} dengan {b} = {a / b}",
                    f"Bulatkan ke bawah: floor({a / b})",
                    f"Hasil = {nilai}"
                ]

    except Exception as e:
        hasil['error'] = f"Terjadi kesalahan: {str(e)}"

    hasil['operasi'] = operasi
    return hasil