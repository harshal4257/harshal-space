class HashTable:
    def __init__(self):
        self.size = int(input("Enter the Size of the hash table: "))
        self.table = [0] * self.size
        self.element_count = 0
        self.comparisons = 0

    def is_full(self):
        return self.element_count == self.size

    def hash_function(self, element):
        return element % self.size

    def quadratic_probing(self, element, position):
        limit = 50
        i = 1
        while i <= limit:
            new_position = (position + i**2) % self.size
            if self.table[new_position] == 0:
                return True, new_position
            i += 1
        return False, None

    def insert(self, element):
        if self.is_full():
            print("Hash Table Full")
            return False

        position = self.hash_function(element)
        if self.table[position] == 0:
            print(f"Element {element} at position {position}")
            self.table[position] = element
            self.element_count += 1
            return True
        else:
            print(f"Collision has occurred for element {element} at position {position}, finding new position.")
            stored, position = self.quadratic_probing(element, position)
            if stored:
                self.table[position] = element
                self.element_count += 1
                return True
            return False

    def search(self, element):
        position = self.hash_function(element)
        self.comparisons += 1
        if self.table[position] == element:
            return position
        else:
            limit = 50
            i = 1
            new_position = position
            while i <= limit:
                new_position = (position + i**2) % self.size
                self.comparisons += 1
                if self.table[new_position] == element:
                    return new_position
                elif self.table[new_position] == 0:
                    return False
                i += 1
            return False

    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = 0
            print(f"Element {element} is deleted")
            self.element_count -= 1
        else:
            print("Element is not present in the Hash Table")

    def display(self):
        print("\n")
        for i in range(self.size):
            print(f"{i} = {self.table[i]}")
        print("The number of elements in the Table are: ", self.element_count)


if __name__ == "__main__":
    table1 = HashTable()
    table1.insert(12)
    table1.insert(26)
    table1.insert(31)
    table1.insert(17)
    table1.insert(90)
    table1.insert(28)
    table1.insert(88)
    table1.insert(40)
    table1.insert(77)
    table1.display()

    print("\nThe position of element 31 is:", table1.search(31))
    print("The position of element 28 is:", table1.search(28))
    print("The position of element 90 is:", table1.search(90))
    print("The position of element 77 is:", table1.search(77))
    print("The position of element 1 is:", table1.search(1))

    print("\nTotal number of comparisons done for searching:", table1.comparisons)

    table1.remove(90)
    table1.remove(12)
    table1.display()
