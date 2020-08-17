cod1,n1,v1 = raw_input().split()
n1, v1 = [int(n1), float(v1)]
cod2,n2,v2 = raw_input().split()
n2, v2 = [int(n2), float(v2)]

print 'VALOR A PAGAR: R$ {0:.2f}'.format((v1*n1+v2*n2))
