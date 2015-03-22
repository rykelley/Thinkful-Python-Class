__author__ = 'Ryan'
time = 0
population = 1000
growth_rate = 0.21
while population < 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1