class Catalog_Node:
    parent = ''
    name = ''

    def __init__(self, input_str:str) -> None:
        input_str = input_str.split(',')
        self.name = input_str[0]
        self.parent = input_str[1]

    def find_catalog_node(self, node_list:list, name):
        for node in node_list:
            if node.name == name:
                return node
        return None

    def calculate_depth(self, node_list:list)->int:
        depth = 0
        current_parent = self.find_catalog_node(node_list, self.parent)

        while current_parent != None and current_parent.name != 'None':
            current_parent = self.find_catalog_node(node_list, current_parent.parent)
            depth += 1
        return depth

    def get_children_as_list(self,node_list:list)->list:
        children = []

        for node in node_list:
            if node.parent == self.name:
                children.append(node)
        
        return children
    
    def sort_children(self):
        pass

    def node_str(self, node_list:list) -> str:
        return ('-'*self.calculate_depth(node_list)) + self.name

def main():
    listing_count = int(input())
    catalog = [Catalog_Node(input()) for idx in range(listing_count)]
    catalog = sorted(catalog, key = lambda x : (x.calculate_depth(catalog), x.name))

    catalog_sorted = []
    
    is_catalog_sorted = False

    while not is_catalog_sorted:

        pass

    for n in catalog:
        print(n.node_str(catalog))
        
if __name__ == '__main__':
    main()