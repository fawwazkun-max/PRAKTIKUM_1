hero = ["Zilong", "Ling", "Baxia", "Wanwan", "Chang'e"]
army = 958730
total_hero = len(hero)

print(f"Jumlah pasukan yang dibawa Yu Zhong = {army}")
print(f"Jumlah pahlawan = {total_hero}")

mission = army // total_hero

print(f"Jumlah pasukan yang harus dikalahkan setiap pahlawan adalah {mission} pasukan")