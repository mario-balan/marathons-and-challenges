a,b,c = map(float, raw_input().split())

print 'TRIANGULO: {0:.3f}'.format((a * c) / 2)
print 'CIRCULO: {0:.3f}'.format(3.14159 * c**2)
print 'TRAPEZIO: {0:.3f}'.format(c * (a + b) / 2)
print 'QUADRADO: {0:.3f}'.format(b**2)
print 'RETANGULO: {0:.3f}'.format(a * b)
