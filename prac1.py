class HashTable:
    def __init__(self):
        self.size = int(input("Enter the Size of the hash table: "))
        self.table = [0] * self.size
        self.elementCount = 0
        self.comparisons = 0

    def isFull(self):
        return self.elementCount == self.size

    def hashFunction(self, element):
        return element % self.size

    def insert(self, element):
        if self.isFull():
            print("Hash Table Full")
            return False

        isStored = False
        position = self.hashFunction(element)

        if self.table[position] == 0:
            self.table[position] = element
            print(f"Element {element} at position {position}")
            isStored = True
            self.elementCount += 1
        else:
            print(f"Collision occurred for element {element} at position {position}. Finding new Position.")
            while self.table[position] != 0:
                position += 1
                if position >= self.size:
                    position = 0
            self.table[position] = element
            isStored = True
            self.elementCount += 1

        return isStored

    def search(self, element):
        position = self.hashFunction(element)
        self.comparisons += 1

        if self.table[position] == element:
            return position

        isFound = False
        temp = position - 1

        while position < self.size:
            if self.table[position] != element:
                position += 1
                self.comparisons += 1
            else:
                return position

        position = temp

        while position >= 0:
            if self.table[position] != element:
                position -= 1
                self.comparisons += 1
            else:
                return position

        if not isFound:
            print("Element not found")
            return False

    def remove(self, element):
        position = self.search(element)

        if position is not False:
            self.table[position] = 0
            print(f"Element {element} is Deleted")
            self.elementCount -= 1
        else:
            print("Element is not present in the Hash Table")
            return

    def display(self):
        print("\n")
        for i in range(self.size):
            print(f"{i} = {self.table[i]}")
        print(f"The number of elements in the Table are: {self.elementCount}")


# Main function
table1 = HashTable()

# Storing elements in the table
table1.insert(12)
table1.insert(26)
table1.insert(31)
table1.insert(17)
table1.insert(90)
table1.insert(28)
table1.insert(88)
table1.insert(40)
table1.insert(77)  # Element that causes collision at position 0

# Displaying the Table
table1.display()
print()

# Printing position of elements
print(f"The position of element 31 is: {table1.search(31)}")
print(f"The position of element 28 is: {table1.search(28)}")
print(f"The position of element 90 is: {table1.search(90)}")
print(f"The position of element 77 is: {table1.search(77)}")
print(f"The position of element 1 is: {table1.search(1)}")

# Total number of comparisons done for searching
print(f"\nTotal number of comparisons done for searching: {table1.comparisons}\n")

# Removing elements from the table
table1.remove(90)
table1.remove(12)

# Displaying the modified table
table1.display()
