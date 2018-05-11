def persistence(n):
    count = 0
    while len(str(n)) > 1:
        m = 1
        for digit in str(n):
            m *= int(digit)
        count += 1
        n = m
    print (count)
    return count

persistence(39)
persistence(4)
persistence(25)
persistence(999)