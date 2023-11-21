def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(7))
    print(spam(0))
    

except ZeroDivisionError:
    print('Error: Invalid argument.')