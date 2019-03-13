def spam(divideBy):
    try: #will try to perform operation
        return 42 / divideBy
    except ZeroDivisionError: #if it fails and yeilds the error message proceeding the except statement then it will perform the following code
        print('Error: Invalid Argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


