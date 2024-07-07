from functions import tsp_algorithm, haversine_formula
from circuit_coordinates import circuits_2024

coordenadas = [circuit["coordinates"] for circuit in circuits_2024]
route = tsp_algorithm(coordenadas)
total = 0
distance = 0
total_temporada = 0
total_novo_caminho = 0

for i, item in enumerate(circuits_2024):
    print("Corrida", i,"->", item["name"])
    if i != len(circuits_2024) - 1:
        distance = haversine_formula(item["coordinates"], circuits_2024[i+1]["coordinates"])
        total = total + distance
        print("{} - Distância até a próxima corrida: {:.2f}Km.".format(i, distance))
    else:
        total_temporada = total
        print("Distância total da temporada: {:.2f}Km".format(total))

print("################################################")

total = 0
distance = 0
route.pop()

for i,item in enumerate(route):
    print("Corrida", i,"->", circuits_2024[item]["name"])
    if i != len(route) - 1:
        distance = haversine_formula(circuits_2024[item]["coordinates"], circuits_2024[route[i+1]]["coordinates"])
        total = total + distance
        print("{} - Distância até a próxima corrida: {:.2f}Km.".format(i, distance))
    else:
        total_novo_caminho = total
        print("Distância total da temporada: {:.2f}Km".format(total))

print("################################################")

print("O quanto melhoramos? {:.2f}Km".format(total_temporada-total_novo_caminho))
