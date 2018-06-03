nested_list = [1, 2, 3,[4]]


def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):

                yield element

    except TypeError:

        yield nested



print(list(flatten(nested_list)))



