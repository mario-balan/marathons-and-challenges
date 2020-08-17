x = int(raw_input())

print x
print x / 100,'nota(s) de R$ 100,00'
x = x % 100
print x / 50,'nota(s) de R$ 50,00'
x = x % 50
print x / 20,'nota(s) de R$ 20,00'
x = x % 20
print x / 10,'nota(s) de R$ 10,00'
x = x % 10
print x / 5,'nota(s) de R$ 5,00'
x = x % 5
print x / 2,'nota(s) de R$ 2,00'
x = x % 2
print x,'nota(s) de R$ 1,00'
