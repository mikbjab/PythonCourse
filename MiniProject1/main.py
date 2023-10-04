import random


def random_point():
    x=random.uniform(-1,1)
    y = random.uniform(-1, 1)
    return [x,y]


def pi_monte_carlo(number_points):
    points_inside=0
    for i in range(number_points):
        point=random_point()
        if point[0]**2+point[1]**2<=1:
            points_inside+=1
    return points_inside*4/number_points


print(pi_monte_carlo(10000000))

