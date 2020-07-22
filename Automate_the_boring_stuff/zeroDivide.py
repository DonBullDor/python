def spam(diveBy):
    try:
        return 42 / diveBy
    except ZeroDivisionError:
        print('invalid argument')


print(spam(2))
print(spam(42))
print(spam(0))