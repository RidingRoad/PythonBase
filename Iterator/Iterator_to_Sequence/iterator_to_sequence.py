import random
class TestIterator(object):
    def __init__(self):
        self.value = 0

    def __next__(self):
        self.value = self.value + random.randrange(12, 100)
        if self.value > 1000:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self



    
if __name__ == "__main__":
    test = TestIterator()
    # using the list() to make the iterator being a sequence
    print(list(test))

