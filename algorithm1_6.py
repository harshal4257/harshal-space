<!-- 1st a

1. **Initialization**:
   - Initialize a hash table with a user-defined size.
   - Create an array to store elements. Initialize all slots to 0.
   - Initialize variables to keep track of the number of elements, comparisons, etc.

2. **isFull Function**:
   - Check if the hash table is full by comparing the number of elements with the size of the table.

3. **hashFunction**:
   - Calculate the hash value for an element using the modulo operation with the size of the hash table.

4. **Insert Function**:
   - Check if the hash table is full. If so, print a message and return False.
   - Calculate the hash value for the element.
   - If the slot at the calculated position is empty, store the element there and increment the element count.
   - If there's a collision, linearly probe until an empty slot is found and store the element there. Update the element count.
   - Return True if the element is stored successfully.

5. **Search Function**:
   - Calculate the hash value for the element.
   - Check if the element is present at the calculated position. If yes, return the position.
   - If not found, perform linear probing in both directions until the element is found or the end of the array is reached.
   - Increment the comparison count for each comparison made.
   - If the element is found, return its position; otherwise, print "Element not found" and return False.

6. **Remove Function**:
   - Use the search function to find the position of the element to be removed.
   - If the element is found, set the slot to 0, decrement the element count, and print a message indicating successful deletion.
   - If the element is not found, print "Element is not present in the Hash Table".

7. **Display Function**:
   - Display the elements of the hash table along with their positions.
   - Print the total number of elements in the table.

8. **Main Function**:
   - Create an instance of the HashTable class.
   - Insert elements into the hash table.
   - Display the table.
   - Search for specific elements and print their positions.
   - Print the total number of comparisons made during searching.
   - Remove elements from the table.
   - Display the modified table.
1st b

Below is the algorithm for the provided Python code that implements a hash table with quadratic probing:

1. **Initialization**:
   - Create a class named `HashTable`.
   - Define an `__init__` method to initialize the hash table with user-defined size, initialize the array to store elements, and set counters for element count and comparisons.

2. **is_full Function**:
   - Check if the hash table is full by comparing the number of elements with the size of the table.

3. **hash_function Method**:
   - Calculate the hash value for an element using the modulo operation with the size of the hash table.

4. **quadratic_probing Method**:
   - Implement quadratic probing to handle collisions.
   - Iterate through a limited number of attempts, calculating new positions using a quadratic function until an empty slot is found or the limit is reached.

5. **insert Method**:
   - Check if the hash table is full. If so, print a message and return False.
   - Calculate the hash value for the element.
   - If the slot at the calculated position is empty, store the element there and increment the element count.
   - If there's a collision, use quadratic probing to find a new position and store the element there. Update the element count.
   - Return True if the element is stored successfully, otherwise return False.

6. **search Method**:
   - Calculate the hash value for the element.
   - Check if the element is present at the calculated position. If yes, return the position.
   - If not found, perform quadratic probing until the element is found or the limit is reached.
   - Increment the comparison count for each comparison made.
   - If the element is found, return its position; otherwise, return False.

7. **remove Method**:
   - Use the search method to find the position of the element to be removed.
   - If the element is found, set the slot to 0, decrement the element count, and print a message indicating successful deletion.
   - If the element is not found, print "Element is not present in the Hash Table".

8. **display Method**:
   - Display the elements of the hash table along with their positions.
   - Print the total number of elements in the table.

9. **Main Function**:
   - Create an instance of the HashTable class.
   - Insert elements into the hash table.
   - Display the table.
   - Search for specific elements and print their positions.
   - Print the total number of comparisons made during searching.
   - Remove elements from the table.
   - Display the modified table.

This algorithm describes the overall flow and functionality of the provided Python code for implementing a hash table with quadratic probing collision resolution.

2nd 
Here's the algorithm for the Skip List data structure:

1. **Class Definitions:**
   - Define a class `Node` to represent each node in the Skip List. Each node contains a key and an array called `forward` to store references to nodes at different levels.
   - Define a class `SkipList` to represent the Skip List. This class contains methods to insert, delete, search, and display elements in the Skip List.

2. **Initialize Skip List:**
   - Initialize the Skip List with the maximum level and the probability factor `P` for node levels.
   - Create a header node with a maximum level and initialize its key to a sentinel value (such as -1).
   - Set the current level of the Skip List to 0.

3. **Create New Node:**
   - Define a method `createNode` to create a new node with a specified level and key.

4. **Random Level Generation:**
   - Define a method `randomLevel` to generate a random level for a new node based on the probability factor `P`.

5. **Insertion:**
   - Define a method `insertElement` to insert a new element into the Skip List.
   - Start from the highest level of the Skip List and move forward while the key of the next node is less than the key of the current node.
   - If a node with the same key already exists, handle collisions using quadratic probing to find a suitable position for insertion.
   - Adjust the levels of nodes as needed to maintain the Skip List's properties.

6. **Deletion:**
   - Define a method `deleteElement` to delete an element from the Skip List.
   - Start from the highest level of the Skip List and move forward while searching for the node with the specified key.
   - If the node is found, remove it from the Skip List and adjust the levels of other nodes if necessary.

7. **Search:**
   - Define a method `searchElement` to search for an element in the Skip List.
   - Start from the highest level of the Skip List and move forward while searching for the node with the specified key.
   - If the node is found, return its position; otherwise, indicate that the element is not present.

8. **Display Skip List:**
   - Define a method `displayList` to display the Skip List level by level.
   - Iterate through each level of the Skip List and print the keys of nodes at that level.

9. **Driver Code:**
   - Implement a driver function `main` to test the Skip List operations.
   - Create an instance of the `SkipList` class, insert elements, search for elements, delete elements, and display the Skip List.

This algorithm outlines the basic operations and structure of a Skip List data structure, which allows for efficient searching, insertion, and deletion of elements with an average time complexity of O(log n).

3rd

This program implements a basic binary tree where each node represents a book, chapter, or section. Users can create the tree by adding nodes and display the tree in a level-by-level order.

### Algorithm:

1. **Class Definition:**
   - Define a class `TREE_CLASS` to represent the binary tree.
   - Define a nested structure `bin` to represent each node of the tree, containing the data (book/chapter/section name), and pointers to the left and right child nodes.

2. **Constructor:**
   - Initialize the `root` of the tree to `NULL`.

3. **Create Method:**
   - Allow users to create the tree by adding nodes.
   - Prompt the user to enter the book/chapter/section name.
   - If the tree is empty, set the root to the new node; otherwise, insert the new node into the appropriate position in the tree.

4. **Insert Method:**
   - Recursively traverse the tree to find the correct position to insert the new node.
   - Prompt the user to choose whether to insert the new node to the left or right of the current node.
   - If the chosen side is empty, insert the new node; otherwise, continue the traversal until an empty position is found.

5. **Display Method:**
   - Implement a level-order traversal of the tree to display the nodes level by level.
   - Calculate the height of the tree.
   - Iterate from level 1 to the height and print the nodes at each level.

6. **Main Function:**
   - Display a menu with options to create, display, or exit.
   - Allow users to create the tree and display it.

### Example Usage:
1. The user selects option 1 (Create) and enters book, chapter, and section names.
2. After creating the tree, the user selects option 2 (Display) to see the tree printed level by level.
3. The user can repeat the process or exit by selecting option 3.

This algorithm outlines the steps for creating and displaying a binary tree representing books, chapters, and sections.

4th

This C++ program implements various operations on a binary search tree (BST), such as creation, display, finding the number of nodes on the longest path, finding the minimum value node, changing the tree by swapping nodes, and searching for a node.

### Algorithm:

1. **Class Definition:**
   - Define a class `bintree` to represent the binary search tree.
   - Define a nested structure `node` to represent each node of the tree, containing the data and pointers to the left and right child nodes.

2. **Constructor:**
   - Initialize the `root` of the tree to `NULL` and set the queue indices `front` and `rear` to `-1`.

3. **Creation Method:**
   - Prompt the user to enter elements and create the BST.
   - If the tree is empty, set the root to the new node; otherwise, insert the new node into the appropriate position in the tree.

4. **Insertion Method:**
   - Recursively traverse the tree to find the correct position to insert the new node.
   - Based on the value of the new node, insert it as the left child or right child of the current node.

5. **Display Method (Inorder Traversal):**
   - Perform an inorder traversal of the tree to display its elements in sorted order.

6. **Finding the Longest Path:**
   - Recursively calculate the depth of the left and right subtrees.
   - Return the maximum depth plus one.

7. **Finding the Minimum Value:**
   - Perform an inorder traversal to find the minimum value node in the BST.

8. **Searching for a Node:**
   - Prompt the user to enter the element to be searched.
   - Perform a binary search to find the element, along with its parent node.

9. **Swapping Nodes (Mirroring):**
   - Perform a level-wise traversal of the tree.
   - Swap the left and right children of each node recursively.

10. **Main Function:**
    - Display a menu with options for various operations.
    - Allow users to perform the desired operation on the binary search tree.

### Example Usage:
1. The user selects option 1 (Create) and enters elements to create the binary search tree.
2. After creating the tree, the user can choose to display it (option 2), find the number of nodes on the longest path (option 3), find the minimum value node (option 4), swap nodes (option 5), or search for a node (option 6).
3. The program repeats until the user chooses to exit.

This algorithm outlines the steps for performing various operations on a binary search tree in C++.

5th

This C++ program is designed to convert a prefix expression to a binary expression tree, display the tree in postfix notation using a non-recursive postorder traversal, and then delete the tree nodes to free memory.

### Algorithm:

1. **Node Structure:**
   - Define a structure `node` to represent a binary tree node containing character data and pointers to the left and right children.

2. **Tree Class:**
   - Define a class `tree` to implement operations related to the binary expression tree.
   - Declare a `top` pointer to represent the root of the binary tree.
   - Implement methods to:
     - Convert the prefix expression to a binary expression tree (`expression`).
     - Display the tree in preorder notation (`display`).
     - Perform a non-recursive postorder traversal and print the expression (`non_rec_postorder`).
     - Delete the tree nodes to free memory (`del`).

3. **Stack Class:**
   - Define a `stack1` class to implement stack operations for storing tree nodes during the construction of the binary tree.

4. **Expression Conversion:**
   - Read the prefix expression from the user.
   - Use a stack to construct the binary expression tree from the prefix expression.

5. **Postorder Traversal:**
   - Perform a non-recursive postorder traversal using two stacks.
   - Push the root node onto the first stack.
   - Pop nodes from the first stack, push them onto the second stack, and push their left and right children onto the first stack.
   - Pop nodes from the second stack and print their data to get the postfix expression.

6. **Node Deletion:**
   - Implement a recursive function to delete the tree nodes in a postorder manner to ensure all child nodes are deleted before their parents.

7. **Main Function:**
   - Create a `tree` object.
   - Prompt the user to enter the prefix expression.
   - Convert the prefix expression to a binary tree, display it in postfix notation, and then delete the tree nodes.

### Example Execution:

- User inputs the prefix expression `*+ab-cd`.
- The program converts the expression to a binary tree and displays it in postfix notation (`ab+cd-*`).
- Finally, it deletes the nodes of the tree.

This algorithm outlines the steps for converting a prefix expression to a binary expression tree, performing a non-recursive postorder traversal, and deleting the tree nodes in C++.


6th

This C++ program implements Depth First Search (DFS) traversal on a graph represented using an adjacency matrix. Here's how the program works:

1. **Graph Representation:**
   - The graph is represented using an adjacency matrix `g[][]`, where `g[i][j]` is set to `TRUE` if there is an edge between vertex `i` and vertex `j`.
   - The class `Gdfs` contains member variables `g[][]` for the adjacency matrix and an array `v[]` to keep track of visited vertices.

2. **Constructor and Destructor:**
   - The constructor initializes the adjacency matrix and the visited array.
   - The destructor clears the adjacency matrix and the visited array.

3. **Graph Creation:**
   - The `create()` method prompts the user to input edges of the graph until `-99` is entered.
   - Each entered edge is marked in the adjacency matrix.

4. **DFS Traversal:**
   - The `Dfs(int v1)` method performs the Depth First Search traversal from vertex `v1`.
   - It marks the current vertex as visited and recursively explores its adjacent vertices.
   - The visited vertices are printed in the order they are traversed.

5. **Main Function:**
   - Creates a `Gdfs` object and calls the `create()` method to input the graph.
   - Displays the adjacency matrix of the graph.
   - Prompts the user to enter the starting vertex for DFS traversal.
   - Calls the `Dfs()` method with the entered starting vertex.
   - Prints the total number of nodes visited during DFS traversal.

### Example Execution:

1. User inputs edges of the graph.
2. The adjacency matrix of the graph is displayed.
3. User inputs the starting vertex for DFS traversal.
4. DFS traversal is performed from the entered vertex.
5. The visited vertices are printed, and the total number of visited nodes is displayed.

This program demonstrates how to perform DFS traversal on a graph represented using an adjacency matrix in C++.

 -->
