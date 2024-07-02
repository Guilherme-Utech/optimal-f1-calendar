import math

def haversine_formula(c1, c2):
    R = 6371.0

    latitude_1 = math.radians(c1[0])
    longitude_1 = math.radians(c1[1])

    latitude_2 = math.radians(c2[0])
    longitude_2 = math.radians(c2[1])

    diference_latitude = latitude_1 - latitude_2
    diference_longitude = longitude_1 - longitude_2

    a = math.sin(diference_latitude / 2)**2 + math.cos(latitude_1) * math.cos(latitude_2) * math.sin(diference_longitude / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

# coord1 = [26.0325, 50.5106]  # Bahrain International Circuit
# coord2 = [21.6225, 39.1108]  # Jeddah Corniche Circuit

# distancia = haversine_formula(coord1, coord2)
# print(f"A distância entre os dois circuitos é de {distancia:.2f} km")

