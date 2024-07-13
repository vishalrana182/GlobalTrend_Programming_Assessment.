def error_handling(i, j):
    try:
        result = i / j
        return result
    except ZeroDivisionError:
        return "0 as divisor is not allowed"


i = int(input())
j = int(input())

result = error_handling(i, j)
print(result)
