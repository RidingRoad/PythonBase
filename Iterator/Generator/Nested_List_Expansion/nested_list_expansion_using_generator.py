
# nested list
nested = [[1, 2], [3, 4], [5]]

# using the generator to expand the nested list,but it use two fors (only for 2 levels nested list)

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


print(list(flatten(nested)))