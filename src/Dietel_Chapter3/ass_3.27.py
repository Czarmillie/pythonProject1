current_population = 8000000000
growth_rate = 1.02

print("Year\tWorld Population\tPopulation Increase")

for year in range(1, 101):
    population = current_population * (growth_rate ** year)
    increase = population - current_population
    print(f"{year}\t\t\t{int(population)}\t\t\t{int(increase)}")

    if population >= current_population * 2:
        print(f"Population will be double in year {year}")
    if population >= current_population * 4:
        print(f"Population will be quadruple in year {year}")