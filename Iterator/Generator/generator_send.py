def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

