x,n = map(int,raw_input().split())

if x == 1:
    total = 4.00 * n
elif x == 2:
    total = 4.50 * n
elif x == 3:
    total = 5.00 * n
elif x == 4:
    total = 2.00 * n
else:
    total = 1.50 * n
    
print 'Total: R$ {0:.2f}'.format(total)
