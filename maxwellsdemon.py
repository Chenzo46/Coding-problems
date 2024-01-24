import decimal
from decimal import Decimal

class part:
    mass = 0.0
    position = 0.0
    velocity = 0.0
    def __init__(self, mass, position, velocity) -> None:
        self.mass = mass
        self.position = position
        self.velocity = velocity
        #Decimal(my_float).quantize(Decimal('0.000001'), rounding=decimal.ROUND_HALF_UP)
        pass

class collision:
    a = part(0, 0, 0)
    b = part(0, 0, 0)
    col_pos = 0
    time = 0
    def __init__(self, a, b, col_pos, time) -> None:
        self.a = a
        self.b = b
        self.col_pos = col_pos
        self.time = time
        #Decimal(my_float).quantize(Decimal('0.000001'), rounding=decimal.ROUND_HALF_UP)
        pass

def sort_part(part_list:list):
    new_cool_list = []
    new_cool_list = sorted(part_list, key = lambda x : x.position)
    return new_cool_list

def calc_next_collision(part_list:list):
    new_cool_list = []

    #left wall; dont go beyond it, there is nothing out there
    if part_list[0].velocity < 0:
        time_left_wall_collision = part_list[0].position/abs(part_list[0].velocity)
        new_cool_list.append(collision(part(0, 0, 0), part_list[0], part_list[0].position, time_left_wall_collision))

    #THE AMAZING RIGHT WALLLLLL
    if part_list[len(part_list) - 1].velocity > 0:
        time_right_wall_collision = part_list[0].position/abs(part_list[0].velocity)
        new_cool_list.append(collision(part(0, 1, 0), part_list[len(part_list) - 1], part_list[len(part_list) - 1].position, time_right_wall_collision))

    #Run through the list
    for pep_talk in range(len(new_cool_list) - 1):
        #Use an awesome equation to find when two particles will collide;
        time_of_collision = (part_list[pep_talk].position + part_list[pep_talk + 1].position)/(part_list[pep_talk].velocity - part_list[pep_talk + 1])
        #position_of_collision =
        new_cool_list.append(collision(part_list[pep_talk], part_list[pep_talk + 1], ))




n = input().rstrip()

for cases in range(int(n)):
    #Gets the initial line of input and creates the empty particle list
    idk = input().split()
    num_particles = int(idk[0])
    seconds =  float(idk[1])

    all_particles = []

    #Creates a list with all particles
    for iparticles in range(num_particles):
        cringe_line = list(map(float,input().split()))
        all_particles.append(part(cringe_line[0], cringe_line[1], cringe_line[2]))

    #Sort the list of particles because we hate everything
    all_particles = sort_part(all_particles)



    

