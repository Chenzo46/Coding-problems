def main():
    listing_count = int(input())
    catalog = [input().split(',') for idx in range(listing_count)]
    catalog = dict(catalog)
    
    seen_categories = []
    catalog_sorted = dict()

    for category in catalog.keys():
        if category not in seen_categories:
            # Find all of this category's children and add it to a sorted catalog
            child_categories = list(filter(lambda x: catalog[x] == category, catalog.keys()))
            child_categories.sort()
            parent_count = 0
            current_parent = catalog[category]
            while current_parent != 'None':
                current_parent = catalog[current_parent]
                parent_count += 1
            dashes = ''
            for parents in range(parent_count):
                dashes += '-'
            catalog_sorted[category] = (child_categories, dashes)
            seen_categories.append(category)
        
if __name__ == '__main__':
    main()