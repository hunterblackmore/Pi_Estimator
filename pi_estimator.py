import random

def estimate(n):
    points_circle = 0
    points_total = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            points_circle += 1
        points_total += 1
    return(4 * points_circle/points_total)

while True:
    print('How many points?')
    points = int(input())
    pi = estimate(points);
    print('Pi estimate is ' + str(pi))
    print('Want to estimate again? y or n')
    yorn = input()
    if yorn == 'y':
        print('ok')
    elif yorn == 'n':
        print('bye')
        break
    else:
        print('You didn\'t enter y or n, you get to play again')