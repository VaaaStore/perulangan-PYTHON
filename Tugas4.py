print("Tugas 4")
limit = int(input("Masukkan batas angka: "))
total_ganjil = 0

for i in range(1, limit + 1, 2):
    total_ganjil += i
print(f"Jumlah seluruh bilangan ganjil dari 1 sampai {limit} adalah: {total_ganjil}")
