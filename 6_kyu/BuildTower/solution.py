def tower_builder(n_floors):
    tower = []
    width = (n_floors * 2) - 1
    
    for floor in range(1, 2 * n_floors, 2):
        blocks = floor * '*'
        line = blocks.center(width)
        tower.append(line)
    return tower