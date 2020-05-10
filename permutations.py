def permutations(array, permutation=[]):
    n = len(array)
    if n > 0:
        for i in range(n):
            array_copy = array.copy()
            element = array_copy.pop(i)
            yield from permutations(array_copy, permutation + [element])
    else:
        yield permutation


def circular_permutations(array):
    permutation = [array.pop(0)]
    return permutations(array, permutation)
