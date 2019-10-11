def sum(m, n):
    if n < 0:
        for _ in range(abs(n)):
            m -= 1
    else:
        for _ in range(n):
            m += 1
    return m


def divide(m, n):
    is_negative = False
    count = 0
    if (m < 0 and n > 0) or m > 0 and n < 0:
        is_negative = True
    m = abs(m)
    n = abs(n)

    if m < n:
        return 0
    else:
        while m - n >= 0:
            m -= n
            count += 1
    if is_negative:
        return -count
    else:
        return count


def subtract(m, n):
    if n < 0:
        for _ in range(abs(n)):
            m += 1
    else:
        for _ in range(abs(n)):
            m -= 1
    return m


def multiply(m, n):
    is_negative = False
    count = 0
    if (m < 0 and n > 0) or m > 0 and n < 0:
        is_negative = True
    m = abs(m)
    n = abs(n)

    if n == 0:
        return 0
    else:
        for _ in range(n):
            count += m

    if is_negative:
        return -count
    else:
        return count


def gcd(m, n):
    m = abs(m)
    n = abs(n)

    while n != 0:
        n, m = m % n, n

    return m
