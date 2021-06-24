"""Calculate a max, a min, and a median using only if, for, else"""

def max_min_median(array: list) -> tuple:
    """Calculate a max, a min, and a median
    using only if, for, else"""

    ordered_array = []

    if len(array) < 2:
        ordered_array = array
        median = ordered_array[0]
    else:
        # Sort an array
        for i, element in enumerate(array):

            if i == 0:
                ordered_array.append(element)
            else:
                idx = 0
                for j, new_element in enumerate(ordered_array):
                    if element >= new_element:
                        idx += 1
                    else:
                        idx = j
                        break

                ordered_array.insert(idx, element)

        print(ordered_array)
        length = len(ordered_array)
        median_index = int(length / 2)

        # Calculate a median
        if length % 2 == 0:
            median_1 = ordered_array[median_index - 1]
            median_2 = ordered_array[median_index]
            median = (median_1 + median_2) / 2
        else:
            median = ordered_array[median_index]

    # Calculate a max and a min
    maximum = ordered_array[-1]
    minimum = ordered_array[0]

    return maximum, minimum, median
