def sum(m,n):
    if n < 0:
        for _ in range(abs(n)):
            m -= 1
    else:
        for _ in range(n):
            m += 1         
    return m

def divide(m, n):
    isNegative = False
    count = 0
    if (m < 0 and n > 0) or m > 0 and n < 0 :
        isNegative = True
    m = abs(m)
    n = abs(n)

    if m < n:
        return 0
    else:
        while m - n >= 0:
            m -= n
            count += 1
    if isNegative:
       return -count
    else:
        return count
