
# nested list
nested = [[1, 2], [3, 4,[6,7,8,[10,12]]], [5]]

# using the generator to expand the nested list

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


print(list(flatten(nested)))