from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data["distance matrix"]=[[0, 797, 2156, 563, 880, 521, 1258, 302, 2253, 1829, 1067, 884, 1702, 162, 2070, 1527, 1719, 1597, 1604, 1706, 390],
[797, 0, 2953, 1170, 1677, 1318, 2055, 591, 3050, 2626, 1864, 277, 2499, 769, 1463, 2006, 2516, 2394, 997, 1099, 421],
[2156, 2953, 0, 1783, 1276, 1635, 898, 2458, 97, 423, 1089, 3026, 664, 2280, 1600, 1057, 535, 559, 2182, 2208, 2532],
[563, 1170, 1783, 0, 507, 148, 885, 675, 1880, 1456, 694, 1447, 1697, 497, 2633, 2090, 1346, 1224, 2167, 2269, 953],
[880, 1677, 1276, 507, 0, 359, 752, 1182, 1373, 1325, 187, 1750, 1566, 1004, 2502, 1959, 839, 717, 2036, 2138, 1256],
[521, 1318, 1635, 148, 359, 0, 737, 823, 1732, 1310, 546, 1391, 1551, 645, 2487, 1944, 1198, 1076, 2021, 2123, 897],
[1258, 2055, 898, 885, 752, 737, 0, 1560, 995, 573, 939, 2128, 814, 1382, 1750, 1207, 461, 339, 1284, 1386, 1634],
[302, 591, 2458, 675, 1182, 823, 1560, 0, 2555, 2131, 1369, 868, 2004, 178, 2054, 1511, 2021, 1899, 1588, 1690, 374],
[2253, 3050, 97, 1880, 1373, 1732, 995, 2555, 0, 424, 1186, 3123, 665, 2377, 1601, 1058, 534, 656, 2279, 2305, 2629],
[1829, 2626, 423, 1456, 1325, 1310, 573, 2131, 424, 0, 1512, 2699, 241, 1953, 1177, 634, 958, 608, 1855, 1881, 2205],
[1067, 1864, 1089, 694, 187, 546, 939, 1369, 1186, 1512, 0, 1937, 1753, 1191, 2689, 2146, 652, 904, 2223, 2325, 1443],
[884, 277, 3026, 1447, 1750, 1391, 2128, 868, 3123, 2699, 1937, 0, 2572, 1046, 1536, 2079, 2589, 2467, 844, 822, 494],
[1702, 2499, 664, 1697, 1566, 1551, 814, 2004, 665, 241, 1753, 2572, 0, 1826, 1036, 493, 1199, 849, 1728, 1754, 2078],
[162, 769, 2280, 497, 1004, 645, 1382, 178, 2377, 1953, 1191, 1046, 1826, 0, 2232, 1689, 1843, 1721, 1766, 1868, 552],
[2070, 1463, 1600, 2633, 2502, 2487, 1750, 2054, 1601, 1177, 2689, 1536, 1036, 2232, 0, 543, 2135, 1785, 692, 718, 1680],
[1527, 2006, 1057, 2090, 1959, 1944, 1207, 1511, 1058, 634, 2146, 2079, 493, 1689, 543, 0, 1592, 1242, 1235, 1261, 1585],
[1719, 2516, 535, 1346, 839, 1198, 461, 2021, 534, 958, 652, 2589, 1199, 1843, 2135, 1592, 0, 350, 1745, 1771, 2095],
[1597, 2394, 559, 1224, 717, 1076, 339, 1899, 656, 608, 904, 2467, 849, 1721, 1785, 1242, 350, 0, 1623, 1649, 1973],
[1604, 997, 2182, 2167, 2036, 2021, 1284, 1588, 2279, 1855, 2223, 844, 1728, 1766, 692, 1235, 1745, 1623, 0, 102, 1214],
[1706, 1099, 2208, 2269, 2138, 2123, 1386, 1690, 2305, 1881, 2325, 822, 1754, 1868, 718, 1261, 1771, 1649, 102, 0, 1316],
[390, 421, 2532, 953, 1256, 897, 1634, 374, 2629, 2205, 1443, 494, 2078, 552, 1680, 1585, 2095, 1973, 1214, 1316, 0]]
    data["demands"] = [70, 70, 90, 50, 70, 90, 110, 70, 110, 70, 70, 110, 110, 90, 50, 90, 110, 90, 70, 110]
    data["vehicle_capacities"] = 60
    data["num_vehicles"] = 1
    data["depot"] = 0
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f"Objective: {solution.ObjectiveValue()}")
    total_distance = 0
    total_load = 0
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        plan_output = f"Route for vehicle {vehicle_id}:\n"
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data["demands"][node_index]
            plan_output += f" {node_index} Load({route_load}) -> "
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id
            )
        plan_output += f" {manager.IndexToNode(index)} Load({route_load})\n"
        plan_output += f"Distance of the route: {route_distance}m\n"
        plan_output += f"Load of the route: {route_load}\n"
        print(plan_output)
        total_distance += route_distance
        total_load += route_load
    print(f"Total distance of all routes: {total_distance}m")
    print(f"Total load of all routes: {total_load}")


def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data["demands"]), data["num_vehicles"], data["depot"]
    )

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        return 0

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data["demands"][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data["vehicle_capacities"],  # vehicle maximum capacities
        True,  # start cumul to zero
        "Capacity",
    )

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.FromSeconds(1)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)


if __name__ == "__main__":
    main()
