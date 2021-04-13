"""
Print only first, fourth, seventh numbers
when you enter 10 numbers.
"""
digits = input("Enter 10 numbers with spaces:")
digits = [int(n) for n in digits.split()]
assert(len(digits)) == 10, "The number of digits is not 10"
print("{}, {}, {}".format(digits[0], digits[3], digits[6]))
