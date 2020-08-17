x,y= map(int,raw_input().split('.'))

print 'NOTAS:'
print x / 100,'nota(s) de R$ 100.00'
x = x % 100
print x / 50,'nota(s) de R$ 50.00'
x = x % 50
print x / 20,'nota(s) de R$ 20.00'
x = x % 20
print x / 10,'nota(s) de R$ 10.00'
x = x % 10
print x / 5,'nota(s) de R$ 5.00'
x = x % 5
print x / 2,'nota(s) de R$ 2.00'
x = x % 2

print 'MOEDAS:'
print x,'moeda(s) de R$ 1.00'
print y / 50,'moeda(s) de R$ 0.50'
y = y % 50
print y / 25,'moeda(s) de R$ 0.25'
y = y % 25
print y / 10,'moeda(s) de R$ 0.10'
y = y % 10
print y / 5,'moeda(s) de R$ 0.05'
y = y % 5
print y,'moeda(s) de R$ 0.01'
