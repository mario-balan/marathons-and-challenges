import math
x1, y1 = map(float, raw_input().split())
x2, y2 = map(float, raw_input().split())

print '{0:.4f}'.format(math.sqrt((x2-x1)**2+(y2-y1)**2))
