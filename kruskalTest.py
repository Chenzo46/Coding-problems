from math import inf
def kruskal_test(nodes) -> list:
    #get smallest weight node pair(1), check if it creates a loop(2), if not add it to the tree(3)

    finished = False

    temp_nodes = sorted(nodes, key = lambda x: x[1])
    blank_nodes = [sorted(nodes[nodes.index(i)][0]) for i in nodes]
    branches = []
    while not finished:

        # 1)
        smallest = temp_nodes[0]
        # 2)
        concat_pair = smallest[0]
        blank_branches = [sorted(branches[branches.index(i)][0]) for i in branches]
        for i in branches:
            concat_temp = i[0]
            if concat_pair[0] in concat_temp:
                temp1 = concat_pair.replace(concat_pair[0], '')
                temp2 = concat_temp.replace(concat_pair[0], '')
                if sorted(temp1.strip() + " " + temp2.strip()) in blank_branches:
                    finished = True
            elif concat_pair[2] in concat_temp:
                temp1 = concat_pair.replace(concat_pair[2], '')
                temp2 = concat_temp.replace(concat_pair[2], '')
                if sorted(temp1.strip() + " " + temp2.strip()) in blank_branches:
                    finished = True
        if finished:
            break

        # 3)
        branches.append(smallest)
        temp_nodes.remove(smallest)

                
    return branches

def get_quickest_route(min_spanning_tree = list, from_to = str) -> list:
    start = from_to[0]
    end = from_to[2]

    min_spanning_tree.sort(key=lambda x: x[1])

    current = start
    path = []
    working = True
    prev_path = []
    while working:
        
        s = []
        smallest = inf
        num_of_paths = 0
        for i in min_spanning_tree:
            if current in i[0] and i[1] < smallest and not s == prev_path:
                num_of_paths += 1
                s = i
                smallest = i[1]
                if end in i[0]:
                    working = False
        if s == []:
            current = prev_path[0].replace(current, '').strip()
            min_spanning_tree.remove(s)
        else:
            path.append(s)
            current = s[0].replace(current, '').strip()
            prev_path = s
            #min_spanning_tree.remove(s)
        
    return path
    


if __name__ == '__main__':
    nodes = [['M F', 3], ['F D', 2], ['F B', 4], ['B D', 35]] #(To, from, weight),...
    kruskal_branches = kruskal_test(nodes)
    print(kruskal_branches)
    #M to D
    path = 'M B'
    print(get_quickest_route(kruskal_branches, path))


    #dijkstra_test(nodes[start_node], nodes)