raw_input() # Just to skip first input, since it is not used for any computation
b = float("{0:.2f}".format(input()))
c = float("{0:.2f}".format(input()))
print 'TOTAL = R$ {0:.2f}'.format(b + 0.15*c)
