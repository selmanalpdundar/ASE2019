from flakon import JsonBlueprint
from flask import Flask, request, jsonify

cacl = JsonBlueprint('cacl', __name__)


@cacl.route('/sum')
def sum():
    # http:://127.0.0.1:5000/sum/divice?m=11&n=11
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1
    return jsonify({'Result': str(result)})


@cacl.route('/divide')
def divide():
    # http:://127.0.0.1:5000/calc/divice?m=11&n=11
    isNegative = False
    count = 0
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    if (m < 0 and n > 0) or m > 0 and n < 0:
        isNegative = True

    m = abs(m)
    n = abs(n)
    result = 0
    if m < n:
        result = 0
    else:
        while m - n >= 0:
            m -= n
            count += 1
    if isNegative:
        result = -count
    else:
        result = count
    return jsonify({"Result ": str(result)})


@cacl.rout('subtract')
def subtract():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    result = m
    if n < 0 and m < 0:
        for i in range(abs(n)):
            result += 1
    elif n < 0 and m > 0:
        for i in range(n):
            result += 1

    return jsonify({'Result': str(result)})


@cacl.route('multiply')
def multiply():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
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


@cacl.route('gcd')
def gcd():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    while n != 0:
        n, m = m % n, n

    return m
