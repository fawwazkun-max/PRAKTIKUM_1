#include <stdio.h>

int main()
{
    char *hero[] = {"Zilong", "Ling", "Baxia", "Wanwan", "Chang'e"};
    int army = 958730;
    int total_hero = sizeof(hero) / sizeof(hero[0]);

    printf("Jumlah pasukan yang dibawa Yu Zhong = %d\n", army);
    printf("Jumlah pahlawan = %d\n", total_hero);

    int mission = army / total_hero;

    printf("Jumlah pasukan yang harus dikalahkan setiap pahlawan adalah %d pasukan\n", mission);
    return 0;
}