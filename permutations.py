def permutations(array, permutation=[]):
    """Generates all possible permutations of an array.

    Args:
        array: An array

    Yields:
        All possible permutations of the array
    """
    if array:
        n = len(array)
        for index in range(n):
            value = array.pop(index)
            yield from permutations(array, permutation + [value])
            array.insert(index, value)
    else:
        yield permutation


def circular_permutations(array):
    """Generates all possible circular permutations of an array.

    Args:
        array: An array

    Yields:
        All possible circular permutations of the array
    """
    return permutations(array[1:], [array[0]])
