#      in python 2.7:
# input() = eval(raw_input())
a = float("{0:.1f}".format(eval(raw_input())))        
b = float("{0:.1f}".format(input()))                  
print 'MEDIA = {0:.5f}'.format(((3.5*a) + (7.5*b))/11)
