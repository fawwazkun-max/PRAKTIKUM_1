import math

lap = 5
distance = 14

print("Diketahui :")
print(f"Pak Dengklek mengelilingi taman = {lap} Putaran")
print(f"Jarak tempuh Pak Dengklek = {distance} Kilometer")
print()

circumference = distance / lap
radius = circumference / (2 * math.pi)

print("Jawaban :")
print(f"Jari-jari taman yang dikelilingi Pak Dengklek adalah {radius:.2f} Kilometer")