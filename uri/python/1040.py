# -*- coding: utf-8 -*-

a,b,c,d = map(float,raw_input().split())

media = (a*2.0 + b*3.0 + c*4.0 + d)/10.0
print 'Media: {0:.1f}'.format(media)

if (media >= 7):
    print 'Aluno aprovado.'
elif (media < 5):
    print 'Aluno reprovado.'

else:

    print 'Aluno em exame.'
    exame = float(raw_input())
    print 'Nota do exame: {0:.1f}'.format(exame)
    media_final = (media + exame) / 2

    if (media_final >= 5):
        print 'Aluno aprovado.'
    else:
        print 'Aluno reprovado.'
    print 'Media final: {0:.1f}'.format(media_final)
    



''' PROBLEMA DADO A CONFUSÕES DE ARREDONDAMENTO EM PYTHON:

>>> decimal.Decimal((2*2.0 + 3*6.5 + 4*4.0 + 1*9.0) / 10)
Decimal('4.8499999999999996447286321199499070644378662109375')

>>> decimal.Decimal(0.2*2.0 + 0.3*6.5 + 0.4*4.0 + 0.1*9.0,1)
Decimal('4.85000000000000053290705182007513940334320068359375')

# a função abaixo arredondava para cima:
# media = round(0.2*a + 0.3*b + 0.4*c + 0.1*d)
'''

