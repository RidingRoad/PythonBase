
def flatten(nested):
    try:
        try:
            nested +  ""
        except TypeError:
            pass
        else:raise TypeError  # 在没有发生异常的情况下会触发
        for sublist in nested:
            for element in flatten(sublist):

                yield element

    except TypeError:

        yield nested

    return list(flatten(nested))



