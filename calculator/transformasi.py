import math

def hitung_transformasi(data):
    kategori = data.get('kategori')
    hasil = {}

    try:
        # =====================
        # KONVERSI BASIS
        # =====================
        if kategori == 'basis':
            angka = data.get('angka', '0').strip()
            dari = data.get('dari')

            if dari == 'decimal':
                n = int(angka)
            elif dari == 'binary':
                n = int(angka, 2)
            elif dari == 'octal':
                n = int(angka, 8)
            elif dari == 'hex':
                n = int(angka, 16)

            hasil['decimal'] = n
            hasil['binary'] = bin(n)[2:]
            hasil['octal'] = oct(n)[2:]
            hasil['hex'] = hex(n)[2:].upper()
            hasil['ringkasan'] = f"Konversi basis: {angka} ({dari})"
            hasil['langkah'] = [
                f"Input: {angka} dalam basis {dari}",
                f"Konversi ke Decimal: {n}",
                f"Konversi ke Binary: {bin(n)[2:]}",
                f"Konversi ke Octal: {oct(n)[2:]}",
                f"Konversi ke Hexadecimal: {hex(n)[2:].upper()}"
            ]

        # =====================
        # KONVERSI SUHU
        # =====================
        elif kategori == 'suhu':
            nilai = float(data.get('nilai', 0))
            dari = data.get('dari')

            if dari == 'celsius':
                c = nilai
                hasil['langkah'] = [
                    f"Input: {nilai} °C",
                    f"Ke Fahrenheit: ({nilai} × 9/5) + 32 = {round((nilai * 9/5) + 32, 2)} °F",
                    f"Ke Kelvin: {nilai} + 273.15 = {round(nilai + 273.15, 2)} K",
                    f"Ke Réamur: {nilai} × 4/5 = {round(nilai * 4/5, 2)} °Ré"
                ]
            elif dari == 'fahrenheit':
                c = (nilai - 32) * 5/9
                hasil['langkah'] = [
                    f"Input: {nilai} °F",
                    f"Ke Celsius: ({nilai} - 32) × 5/9 = {round(c, 2)} °C",
                    f"Ke Kelvin: {round(c, 2)} + 273.15 = {round(c + 273.15, 2)} K",
                    f"Ke Réamur: {round(c, 2)} × 4/5 = {round(c * 4/5, 2)} °Ré"
                ]
            elif dari == 'kelvin':
                c = nilai - 273.15
                hasil['langkah'] = [
                    f"Input: {nilai} K",
                    f"Ke Celsius: {nilai} - 273.15 = {round(c, 2)} °C",
                    f"Ke Fahrenheit: ({round(c, 2)} × 9/5) + 32 = {round((c * 9/5) + 32, 2)} °F",
                    f"Ke Réamur: {round(c, 2)} × 4/5 = {round(c * 4/5, 2)} °Ré"
                ]
            elif dari == 'reamur':
                c = nilai * 5/4
                hasil['langkah'] = [
                    f"Input: {nilai} °Ré",
                    f"Ke Celsius: {nilai} × 5/4 = {round(c, 2)} °C",
                    f"Ke Fahrenheit: ({round(c, 2)} × 9/5) + 32 = {round((c * 9/5) + 32, 2)} °F",
                    f"Ke Kelvin: {round(c, 2)} + 273.15 = {round(c + 273.15, 2)} K"
                ]

            hasil['celsius'] = round(c, 2)
            hasil['fahrenheit'] = round((c * 9/5) + 32, 2)
            hasil['kelvin'] = round(c + 273.15, 2)
            hasil['reamur'] = round(c * 4/5, 2)
            hasil['ringkasan'] = f"Konversi suhu: {nilai} {dari}"

        # =====================
        # KONVERSI MATA UANG
        # =====================
        elif kategori == 'mata_uang':
            idr = float(data.get('nilai', 0))
            RATE = {
                'USD': 0.000064,
                'EUR': 0.000059,
                'SGD': 0.000086,
                'MYR': 0.000300,
                'JPY': 0.0096,
                'GBP': 0.000051
            }
            hasil['idr'] = idr
            hasil['konversi'] = {k: round(idr * v, 4) for k, v in RATE.items()}
            hasil['ringkasan'] = f"Konversi mata uang: IDR {idr:,.0f}"
            hasil['langkah'] = [
                f"Input: IDR {idr:,.0f}",
                f"Kurs USD: 1 IDR = {RATE['USD']} USD → {round(idr * RATE['USD'], 4)} USD",
                f"Kurs EUR: 1 IDR = {RATE['EUR']} EUR → {round(idr * RATE['EUR'], 4)} EUR",
                f"Kurs SGD: 1 IDR = {RATE['SGD']} SGD → {round(idr * RATE['SGD'], 4)} SGD",
                f"Kurs MYR: 1 IDR = {RATE['MYR']} MYR → {round(idr * RATE['MYR'], 4)} MYR",
                f"Kurs JPY: 1 IDR = {RATE['JPY']} JPY → {round(idr * RATE['JPY'], 4)} JPY",
                f"Kurs GBP: 1 IDR = {RATE['GBP']} GBP → {round(idr * RATE['GBP'], 4)} GBP",
            ]

        # =====================
        # FAKTORIAL
        # =====================
        elif kategori == 'faktorial':
            n = int(data.get('nilai', 0))
            if n < 0:
                hasil['error'] = "Faktorial tidak bisa untuk bilangan negatif!"
            elif n > 20:
                hasil['error'] = "Masukkan angka maksimal 20!"
            else:
                nilai = math.factorial(n)
                # Buat langkah perkalian
                langkah_kali = ' × '.join(str(i) for i in range(1, n+1)) if n > 0 else '1'
                hasil['nilai'] = nilai
                hasil['rumus'] = f"{n}! = {nilai}"
                hasil['ringkasan'] = f"Faktorial: {n}! = {nilai}"
                hasil['langkah'] = [
                    f"Faktorial {n} ditulis sebagai {n}!",
                    f"Rumus: n! = 1 × 2 × 3 × ... × n",
                    f"{n}! = {langkah_kali}",
                    f"Hasil = {nilai}"
                ]

        # =====================
        # FIBONACCI
        # =====================
        elif kategori == 'fibonacci':
            n = int(data.get('nilai', 0))
            if n < 0:
                hasil['error'] = "Fibonacci tidak bisa untuk bilangan negatif!"
            elif n > 30:
                hasil['error'] = "Masukkan angka maksimal 30!"
            else:
                fib = [0, 1]
                for i in range(2, n+1):
                    fib.append(fib[-1] + fib[-2])
                deret = fib[:n+1]
                hasil['deret'] = deret
                hasil['nilai'] = deret[-1]
                hasil['ringkasan'] = f"Fibonacci ke-{n} = {deret[-1]}"
                hasil['langkah'] = [
                    f"Deret Fibonacci dimulai dari: 0, 1",
                    f"Setiap angka = jumlah dua angka sebelumnya",
                ] + [f"F({i}) = {fib[i-1]} + {fib[i-2]} = {fib[i]}" for i in range(2, min(n+1, 8))] + [
                    f"Fibonacci ke-{n} = {deret[-1]}"
                ]

    except Exception as e:
        hasil['error'] = f"Terjadi kesalahan: {str(e)}"

    hasil['kategori'] = kategori
    return hasil