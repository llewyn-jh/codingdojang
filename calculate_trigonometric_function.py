"""Calculate cosine and sine funtions in person"""

import math

def calculate_trigonometric_function(radian_x: float) -> float:
    """This function refer to Taylor's theorm.
    A remainder for cos or sin at radian_x follows Cauchy's remainder.
    The function has 2 steps. Step1 get a degree of
    Taylor polynomial function at radian_x. Step 2 calculates sin and cos at radian_x
    and return two values
    """

    # Step1: get a degree of Taylor polynomial function at radian_x
    degree = 0
    error = 5 * 1e-6
    upper_limit = radian_x ** degree / math.factorial(degree)
    while upper_limit >= error:
        # Upper limit of Cauchy's remainder for sin or cos at radian_x
        degree += 1
        upper_limit = radian_x ** degree / math.factorial(degree)

    # Step2: Calculate sin, cos at radian_x
    sin = 0
    cos = 0
    for i in range(degree):
        sin += (-1) ** i * radian_x ** ((2 * i) + 1) / math.factorial(2 * i + 1)
        cos += (-1) ** i * radian_x ** (2 * i) / math.factorial(2 * i)

    return sin + cos
