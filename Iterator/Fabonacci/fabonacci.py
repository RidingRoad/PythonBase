class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self




fibs = Fibs()

i = 1
MAX_NUM = 10
for num  in fibs:

    if i < 10:
        print(num,end=' ')
    else:
        break
    i += 1



# the another fabonacci methods

a = 0
b = 1

def fabonacci(c):
    global a
    global b
    a, b = b, a + b
    return a

print()
print(list(map(fabonacci, list(i for i in range(MAX_NUM)))))