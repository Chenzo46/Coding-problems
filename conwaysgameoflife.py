"""
1. Any live cell adjacent to one or zero live cells dies (from loneliness).
2. Any live cell adjacent to two or three live cells lives.
3. Any live cell adjacent to four or more live cells dies (from overcrowding).
4. Any dead cell adjacent to exactly three live cells becomes alive (through reproduction).
"""
class cell:
    row = 0
    column = 0
    alive = 0
    world = []

    def __init__(self, row:int, column:int, alive:int, world):
        self.row = row
        self.column = column
        self.alive = alive
        self.world = world

    def get_adjacent_cell_count(self):
        adjacent_count = 0
        for idx in range(-1,2):
            for jdx in range(-1,2):
                new_row = self.row + idx
                new_column = self.column + jdx
                same_cell = idx == 0 and jdx == 0
                if new_row in range (0,10) and new_column in range(0,10) and not same_cell:
                    adjacent_count += int(self.world[new_row][new_column])
        return adjacent_count
    
def main():
    cases = int(input())
    for case in range(cases):
        generation_count = int(input())
        current_world = [input() for idx in range(10)]
        new_world = []
        for generation in range(generation_count):
            new_world = []
            
            for row,current_line in enumerate(current_world):
                new_line = ''
                for column,alive in enumerate(current_line):
                    current_cell = cell(row, column, int(alive), current_world)
                    adjacent_count = current_cell.get_adjacent_cell_count()
                    new_alive = 0
                    if current_cell.alive == 1:
                        if adjacent_count <= 1 or adjacent_count >= 4:
                            new_alive = 0
                        else:
                            new_alive = 1
                    elif current_cell.alive == 0 and adjacent_count == 3:
                        new_alive = 1
                    new_line += str(new_alive)
                    
                new_world.append(new_line)
            
            current_world = new_world
            print('\n'.join(new_world))

if __name__ == '__main__':
    main()