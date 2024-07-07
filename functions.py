import math
import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

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

def calc_distance_matrix(coordenadas):
    tam = len(coordenadas)
    distance_matrix = np.zeros((tam, tam))

    for i in range(tam):
        for j in range(tam):
            if i != j:
                distance_matrix[i][j] = haversine_formula(coordenadas[i], coordenadas[j])

    return distance_matrix

def tsp_algorithm(coordenadas):
    distance_matrix = calc_distance_matrix(coordenadas)
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return calc_distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        route = []
        index = routing.Start(0)
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))
        return route
    else:
        return None
