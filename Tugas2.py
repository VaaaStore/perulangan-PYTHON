print("Tugas 2")
ulang = int(input("Mau cek berapa angka? "))
for _ in range(ulang):
    angka = int(input("masukan angka: "))
    prima = angka > 1 and all(angka % d != 0 for d in range(2, int(angka**0.5) + 1))
    print(f"Angka {angka} adalah {'PRIMA' if prima else 'BUKAN PRIMA'}\n")
