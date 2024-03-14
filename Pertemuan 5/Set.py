print("\033c")  # To clear the console

# PART 1
# Membuat sebuah set (ada dua cara)
Set_1 = {"Toyota", "Daihatsu", "Honda"}
Set_2 = set(("Toyota", "Daihatsu", "Honda"))

print("Tipe data Set_1 adalah ", type(Set_1))
print("Tipe data Set_2 adalah ", type(Set_2))
print("Data Set_1: ", Set_1)
print("Data Set_2: ", Set_2)
print("....................................")

# Mencetak setiap item dari Set_1
for x in Set_1:
    print(x)
print("....................................")

# Memeriksa panjang set
print(len(Set_1))

# Memeriksa apakah sebuah kunci ada
if "Daihatsu" in Set_1:
    print("Ya, Daihatsu adalah item dalam Set_1.")

# Menambahkan sebuah item
Set_1.add("Mitsubishi")
print(Set_1)

# Menambahkan beberapa item
Set_1.update(["Suzuki", "Mazda", "Nissan"])
print(Set_1)

# Menghapus sebuah item (metode 1)
Set_1.remove("Honda")
print(Set_1)

# Menghapus sebuah item (metode 2)
Set_1.remove("Mazda")
print(Set_1)

# Menghapus (pop) kunci yang dimasukkan terakhir
Set_1.pop()
print(Set_1)

# Mengosongkan set
Set_1.clear()
print(Set_1)

# Menghapus set
del Set_1
print(".............................")

# Gabungan dari dua set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print(".............................")

# Set 1 mengambil salinan semua item dari set 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
