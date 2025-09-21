def balance_check(word):
    """ Check if an inputted word consisting of the characters 'x' and 'y' contains an equal amount of both or not. """
    x_count = 0
    y_count = 0

    for c in word:
        if c == 'x': x_count += 1
        if c == 'y': y_count += 1
    if(x_count == y_count):
        print("True")
    elif (x_count > 0 and y_count == 0) or (x_count == 0 and y_count > 0):
        print("False")
    else:
        print("False")

word = balance_check('xxyy')

