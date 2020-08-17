from math import sqrt

a,b,c = map(float, raw_input().split())

if (a == 0) or (b**2 - 4*a*c < 0):
    print 'Impossivel calcular'
else:
    r1 = (-b + (sqrt(b**2 - 4*a*c))) / (2*a)
    r2 = (-b - (sqrt(b**2 - 4*a*c))) / (2*a)
    print 'R1 = {0:.5f}'.format(r1)
    print 'R2 = {0:.5f}'.format(r2)
