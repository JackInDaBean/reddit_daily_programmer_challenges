import decimal

def calculate_pi():
    """ Calculate the digits of Pi to atleast 30 decimal places - I chose to use the Leibniz formula. """

    # Set precision to 30 decimal places
    decimal.getcontext().prec = 30

    # Numerator in Leibniz is always 4
    NUMERATOR = decimal.Decimal(4.0) 
    denominator = decimal.Decimal(1.0)
    current_calculation = decimal.Decimal(0.0) 
    pi_sum = decimal.Decimal(0.0)

    # Loop must start on 1 to check for odd / even, added 1 to the end so it actually ends on 5 billion.
    for i in range(1, 5_000_000_001):

        current_calculation = (NUMERATOR / denominator)
        denominator += 2

        # If index number is 1, add current calculation and skip to next iteration
        if (i == 1):
            pi_sum = current_calculation
            continue
        
        # If index number is positive then subtract the previous calculation
        elif (i % 2 == 0):
            pi_sum -= current_calculation
            print(pi_sum)

        # If index number is negative then add the previous calculation
        elif (i % 2 != 0):
            pi_sum += current_calculation
            print(pi_sum)

solved_pi = decimal.Decimal(calculate_pi())

print(solved_pi)