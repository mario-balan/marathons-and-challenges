total = int(raw_input())

for i in range(total):

    n = int(raw_input())

    if n > 0:
        if n % 2 == 0:
            print 'EVEN POSITIVE'
        else:
            print 'ODD POSITIVE'
    elif n < 0:
        if n % 2 == 0:
            print 'EVEN NEGATIVE'
        else:
            print 'ODD NEGATIVE'
    else:
        print 'NULL'
