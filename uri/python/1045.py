lados = map(float,raw_input().split())

lados.sort(reverse = True)
a, b, c = [lados[0], lados[1], lados[2]]

if (a >= b + c):
    print 'NAO FORMA TRIANGULO'
elif (a**2 == b**2 + c**2):
    print 'TRIANGULO RETANGULO'
elif (a**2 > b**2 + c**2):
    print 'TRIANGULO OBTUSANGULO'
else:
    print 'TRIANGULO ACUTANGULO'
    
if (a == b and a == c and b ==c):
    print 'TRIANGULO EQUILATERO'
elif (a == b or a == c or b ==c):
    print 'TRIANGULO ISOSCELES'
