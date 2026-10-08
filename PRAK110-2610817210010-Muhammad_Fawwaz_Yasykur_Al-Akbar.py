import math

base = 5
height = 12
side = math.sqrt ((base * base) + (height * height))
perimeter = base + height + side
area = (base * height) / 2

print("Diketahui :")
print(f"Alas = {base} cm")
print(f"Tinggi = {height} cm")
print()
print("Jawab :")
print(f"Sisi A = {base} cm")
print(f"Sisi B = {side:.0f} cm")
print(f"Sisi C = {height} cm")
print(f"Keliling = {perimeter:.0f} cm")
print(f"Luas = {area:.0f} cm")