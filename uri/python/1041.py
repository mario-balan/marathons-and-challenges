x, y = map(float,raw_input().split())

if (x == 0 or y == 0):
    if (x == y):
        print 'Origem'
    elif (y == 0):
        print 'Eixo X'
    else:
        print 'Eixo Y'
elif (y > 0):
    if (x > 0):
        print 'Q1'
    else:
        print 'Q2'
else:
    if (x < 0):
        print 'Q3'
    else:
        print 'Q4'
