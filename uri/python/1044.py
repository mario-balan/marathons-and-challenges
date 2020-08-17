a, b = map(int,raw_input().split())

if (a == b):
    print 'Sao Multiplos'
elif (b > a and b % a == 0):
    print 'Sao Multiplos'
elif (b < a and a % b == 0):
    print 'Sao Multiplos'
else:
    print 'Nao sao Multiplos'
