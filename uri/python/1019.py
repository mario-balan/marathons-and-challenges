s = int(raw_input())

# poderia ter usado o resto, também:

m = s / 60
s = s - m * 60
h = m / 60
m = m - h * 60

print '{}:{}:{}'.format(h,m,s)
