from math import cos, pi, radians

earth_radius = 6_370_000
cases = int(input())

for _ in range(cases):
    theta = float(input())

    n_radius = earth_radius * cos(radians(theta))
    circumfrence = n_radius * 2  * pi
    velocity = circumfrence / 86_400

    print(int(velocity))