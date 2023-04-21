from math import inf
def main():
    # All given costs asociated with each company (Stays constant)
    # index 0-2 air
    # index 3-5 ground
    # cost in dollars per mile per pound, how many minutes in a mile, weight limit in pounds
    company_costs = {
        'A': [0.0105, 0.16, 500, 0.003, 1.1, 5000],
        'B': [0.012, 0.125, 1000, 0.0035, 1.0, 2000],
        'C': [0.095, 0.165, 100, 0.002, 1.05, inf],
        'D': [0.025, 0.15, inf, 0.0025, 1.25, 2500],
        'E': [0.040, 0.13, 750, 0.004, 1.15, inf],
        'F': [0.067, 0.145, inf, 0.0015, 0.95, 3000]
    }

    cases = int(input())

    for case in range(cases):
        total_companies, total_orders = list(map(int,input().split()))
        
        # Company Name, location 1 (l1), location 2 (l2), Mode of transport, Distance between l1 and l2
        companies = [input().split() for company in range(total_companies)] 
        
        # origin, destination, weight of package, Cheapest (C) or Fastest (F) route
        orders = [input().split() for order in range(total_orders)]

        for order in orders:
            total_cost = 0
            total_time = 0
            origin, destination, weight, route_preference = order
            weight = float(weight)
            
            filtered_companies = []
            #For companies that provide both modes of transport, change and choose the stored mode to the better one in repspects to the route preference and weight limit
            for company in companies:
                this_company_costs = company_costs[company[0]]
                
                if company[3] == 'B':
                     if route_preference == 'C':
                        cost_ground = this_company_costs[3] * float(company[4]) * weight
                        cost_air = this_company_costs[0] * float(company[4]) * weight
                        
                        weight_limit_ground = this_company_costs[5]
                        weight_limit_air = this_company_costs[2]

                        if cost_ground < cost_air:
                            company[3] = 'G'
                        else:
                            company[3] = 'A'

                        if weight_limit_ground < weight and weight_limit_air < weight:
                            continue
                        elif weight_limit_ground < weight and company[3] == 'G':
                            company[3] == 'A'
                        elif weight_limit_air < weight and company[3] == 'A':
                            company[3] == 'G'
                        
                        filtered_companies.append(company)
                     elif route_preference == 'F':
                        time_ground = (this_company_costs[4] * float(company[4]))/60
                        time_air = (this_company_costs[1] * float(company[4]))/60
                        
                        weight_limit_ground = this_company_costs[5]
                        weight_limit_air = this_company_costs[2]

                        if time_ground < time_air:
                            company[3] = 'G'
                        else:
                            company[3] = 'A'

                        if weight_limit_ground < weight and weight_limit_air < weight:
                            continue
                        elif weight_limit_ground < weight and company[3] == 'G':
                            company[3] == 'A'
                        elif weight_limit_air < weight and company[3] == 'A':
                            company[3] == 'G'
                        
                        filtered_companies.append(company)
                else:
                    # Otherwise, only check if weight limit is exeeded
                    weight_limit = 0
                    if company[3] == 'A':
                        weight_limit = this_company_costs[2]
                    else:
                        weight_limit = this_company_costs[5]
                    
                    if weight_limit >= weight:
                        filtered_companies.append(company)

            # Remove inferior duplicate companies

            occured_routes = []
            duplicate_routes = []
            
            for company in filtered_companies:
                path = sorted(company[1] + company[2])

                if path in occured_routes and path not in duplicate_routes:
                    duplicate_routes.append(path)
                else:
                    occured_routes.append(path)
            
            for duplicate in duplicate_routes:
                # Find information for same routes
                duplicate_route_options = []
                for company in filtered_companies:
                    path = sorted(company[1] + company[2])

                    if duplicate == path:
                        duplicate_route_options.append(company)
                # Find worst companies in respects to the route preference

                lowest_edge_weight = inf
                bad_duplicates = []
                best_duplicate = []
                for company in duplicate_route_options:
                    this_company_costs = company_costs[company[0]]
                    
                    if route_preference == 'C':
                        edge_weight = this_company_costs[3] * float(company[4]) * weight if company[3] == 'G' else this_company_costs[0] * float(company[4]) * weight

                        if edge_weight < lowest_edge_weight:
                            lowest_edge_weight = edge_weight
                            
                            if best_duplicate != []:
                                bad_duplicates.append(best_duplicate)
                            
                            best_duplicate = company
                        else:
                            bad_duplicates.append(company)
                            
                    elif route_preference == 'F':
                        edge_weight = (this_company_costs[4] * float(company[4])) / 60 if company[3] == 'G' else (this_company_costs[1] * float(company[4])) / 60
                        if edge_weight < lowest_edge_weight:
                            lowest_edge_weight = edge_weight
                            
                            if best_duplicate != []:
                                bad_duplicates.append(best_duplicate)
                            
                            best_duplicate = company
                        else:
                            bad_duplicates.append(company)
                
                #Remove all bad duplicates from filtered list

                for bad_duplicate in bad_duplicates:
                    filtered_companies.remove(bad_duplicate)

            # Now we can finally use Dijkstra's algorithm after all that pain and suffering
            # Make a list of all unique companies so that we can store their asscoiated edge weights in a dictionary

            unique_companies = []
            for company in filtered_companies:
                if company[1] not in unique_companies:
                    unique_companies.append(company[1])
                elif company[2] not in unique_companies:
                    unique_companies.append(company[2])
            edge_weight_map = dict.fromkeys(unique_companies, inf)
            edge_weight_map[origin] = 0

            #Store a list of each connection between two cities that leads to the shortest route from the origin to any other city
            shortest_paths = dict.fromkeys(unique_companies, 'None')

            unvisited = unique_companies.copy()
            
            current_city = origin
            while len(unvisited) > 0:
                
                # Find all possible paths from the current city
                possible_paths = []
                for company in filtered_companies:
                    if current_city in company:
                        temp = company.copy()
                        temp.remove(current_city)
                        possible_paths.append(temp)
                # Update all edge weights
                for company in possible_paths:
                    this_company_costs = company_costs[company[0]]
                    edge_weight = 0

                    if route_preference == 'C':
                        edge_weight = this_company_costs[3] * float(company[3]) * weight if company[2] == 'G' else this_company_costs[0] * float(company[3]) * weight
                    elif route_preference == 'F':
                        edge_weight = (this_company_costs[4] * float(company[3])) / 60 if company[2] == 'G' else (this_company_costs[1] * float(company[3])) / 60
                    
                    edge_weight += edge_weight_map[current_city]

                    previous_edge_weight = edge_weight_map[company[1]]

                    if edge_weight < previous_edge_weight:
                            edge_weight_map[company[1]] = edge_weight
                            shortest_paths[company[1]] = current_city
                
                # Remove current city from unvisited list
                unvisited.remove(current_city)
                # Choose next city to go to
                lowest_edge_weight = inf
                next_city = []

                for city,edge_weight in edge_weight_map.items():

                    if edge_weight < lowest_edge_weight and city in unvisited:
                        lowest_edge_weight = edge_weight
                        next_city = city

                current_city = next_city

                if next_city == destination:
                    break

            # With both the edge weight map and the shortest paths list, create a new list with company information of each route
            # Now we go backwards :)

            final_companies = []

            current_city = destination

            start_found = False

            final_string = []

            while not start_found:
                
                next_city = shortest_paths[current_city]

                path_name = sorted(current_city + next_city)

                company_info = []

                for company in filtered_companies:
                    path = sorted(company[1] + company[2])

                    if path == path_name:
                        company_info = company
                        break
                
                final_companies.insert(0, company_info)

                mode_of_transport = 'ground' if company_info[3] == 'G' else 'air'
                final_string.append(f'{next_city} to {current_city} by {mode_of_transport} with Company {company_info[0]}')

                current_city = next_city

                if shortest_paths[next_city] == 'None':
                    start_found = True

            final_string.reverse()
            # Find and assign the total time and cost to print as information
            if route_preference == 'C':
                total_cost = edge_weight_map[destination]
                # Find total time
                for company in final_companies:
                    this_company_costs = company_costs[company[0]]
                    total_time += (this_company_costs[4] * float(company[4])) / 60 if company[3] == 'G' else (this_company_costs[1] * float(company[4])) / 60
            elif route_preference == 'F':
                total_time = edge_weight_map[destination]
                # Find total cost
                for company in final_companies:
                    this_company_costs = company_costs[company[0]]
                    total_cost += this_company_costs[3] * float(company[4]) * weight if company[3] == 'G' else this_company_costs[0] * float(company[4]) * weight

            total_time = round(total_time,2)
            total_cost = round(total_cost,2)

            # Print out answer in correct format
            print('\n'.join(final_string))
            print(f'Total Hours: {total_time:.2f}')
            print(f'Total Cost: ${total_cost:.2f}')


if __name__ == '__main__':
    main()