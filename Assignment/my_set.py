class MySet:
    def __init__(self):
        self.elements = []

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
            return True
        return False

    def contains(self, element):
        return element in self.elements

    def remove(self, element):
        try:
            self.elements.remove(element)
            return True
        except ValueError:
            return False

    def size(self):
        return len(self.elements)

my_set = MySet()
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(1)

print("Size:", my_set.size())
