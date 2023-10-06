population_wealth = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
wealth_distributed = 0
if sum(population_wealth) < minimum_wealth * len(population_wealth):
    print("No equal distribution possible")
else:
    for index, person in enumerate(population_wealth):
        highest = population_wealth.index(max(population_wealth))
        while population_wealth[index] < minimum_wealth:
            wealth_distributed = minimum_wealth - population_wealth[index]
            population_wealth[index] += wealth_distributed
            population_wealth[highest] -= wealth_distributed
            if population_wealth[highest] == minimum_wealth:
                highest = population_wealth.index(max(population_wealth))

    print(population_wealth)
