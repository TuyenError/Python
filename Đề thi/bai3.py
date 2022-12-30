countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan']
population = [1439323776, 1380004385, 331002651, 273523615, 220892340]

# threecountries = []
# name = ''
# highest = 0

# for i in range(3):
#     threecountries += [input("Nhap dat nuoc thu " + str(i) + ": ")]

# for i in threecountries:
#     if i not in countries:
#         print("Error, bab country name entered")
#         break
#     else:
#         for i in range(len(population)):
#             if (countries[i] in threecountries) and (population[i] > highest):
#                 highest = population[i]
#                 name = countries[i]
# print(name)

countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan']
population = [1439323776, 1380004385, 331002651, 273523615, 220892340]
def getPopulation(name):
    if name not in countries:
        return -1
    for i in range(len(countries)):
        if countries[i] == name:
            return population[i]
country  = input("Nhap nuoc: ")
print(getPopulation(country))
