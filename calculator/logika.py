def hitung_logika(data):
    operasi = data.get('operasi')
    hasil = {}

    try:
        a = data.get('nilai1') == 'true'
        b = data.get('nilai2') == 'true' if data.get('nilai2') else None

        if operasi == 'and':
            nilai = a and b
            hasil['nilai'] = nilai
            hasil['rumus'] = f"{a} AND {b} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: A = {a}, B = {b}",
                "Aturan AND: True hanya jika KEDUA nilai True",
                f"Tabel: True AND True = True, selain itu = False",
                f"Hasil: {a} AND {b} = {nilai}"
            ]

        elif operasi == 'or':
            nilai = a or b
            hasil['nilai'] = nilai
            hasil['rumus'] = f"{a} OR {b} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: A = {a}, B = {b}",
                "Aturan OR: True jika SALAH SATU nilai True",
                f"Tabel: False OR False = False, selain itu = True",
                f"Hasil: {a} OR {b} = {nilai}"
            ]

        elif operasi == 'not':
            nilai = not a
            hasil['nilai'] = nilai
            hasil['rumus'] = f"NOT {a} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: A = {a}",
                "Aturan NOT: membalik nilai boolean",
                f"NOT True = False, NOT False = True",
                f"Hasil: NOT {a} = {nilai}"
            ]

        elif operasi == 'xor':
            nilai = a ^ b
            hasil['nilai'] = nilai
            hasil['rumus'] = f"{a} XOR {b} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: A = {a}, B = {b}",
                "Aturan XOR: True jika nilai A dan B BERBEDA",
                f"Tabel: True XOR False = True, True XOR True = False",
                f"Hasil: {a} XOR {b} = {nilai}"
            ]

        elif operasi == 'nand':
            nilai = not (a and b)
            hasil['nilai'] = nilai
            hasil['rumus'] = f"{a} NAND {b} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: A = {a}, B = {b}",
                f"Langkah 1 - Hitung AND dulu: {a} AND {b} = {a and b}",
                f"Langkah 2 - Balik hasilnya (NOT): NOT {a and b} = {nilai}",
                f"Hasil: {a} NAND {b} = {nilai}"
            ]

        elif operasi == 'nor':
            nilai = not (a or b)
            hasil['nilai'] = nilai
            hasil['rumus'] = f"{a} NOR {b} = {nilai}"
            hasil['langkah'] = [
                f"Diketahui: A = {a}, B = {b}",
                f"Langkah 1 - Hitung OR dulu: {a} OR {b} = {a or b}",
                f"Langkah 2 - Balik hasilnya (NOT): NOT {a or b} = {nilai}",
                f"Hasil: {a} NOR {b} = {nilai}"
            ]

    except Exception as e:
        hasil['error'] = f"Terjadi kesalahan: {str(e)}"

    hasil['operasi'] = operasi
    return hasil