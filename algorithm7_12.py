<!-- 7th
This C++ program demonstrates the use of adjacency list representation to create and display a graph representing a city transport map. Here's a breakdown of how the program works:

1. **Vertex Class (`Vertex`):**
   - Represents each city in the transport map.
   - Contains a string variable `city` to store the name of the city and a vector of `Edge` objects representing the edges from this vertex to other vertices.
   - Provides methods to add an edge (`addEdge`), display edges (`showEdge`), and retrieve the city name (`getCity`).

2. **Edge Class (`Edge`):**
   - Represents an edge between two cities.
   - Contains pointers to the source and destination vertices (`source` and `destination`) and the distance between them (`distance`).
   - Provides methods to retrieve the source, destination, and distance of the edge.

3. **Graph Class (`Graph`):**
   - Manages a collection of vertices and provides methods to insert vertices into the graph and display the adjacency list representation of the graph.
   - Contains a vector of pointers to `Vertex` objects.

4. **Main Function:**
   - Creates instances of the `Vertex` class representing cities in the transport map (Mumbai, Pune, Kolkata, Delhi).
   - Adds edges between cities using the `addEdge` method.
   - Creates a `Graph` object and inserts the vertices into the graph using the `insert` method.
   - Displays the city transport map using the adjacency list representation by calling the `Display` method of the `Graph` class.

### Example Execution:

1. Vertices representing cities are created (Mumbai, Pune, Kolkata, Delhi).
2. Edges representing transportation routes between cities are added.
3. The graph is created, and vertices are inserted into the graph.
4. The adjacency list representation of the graph is displayed, showing the transportation routes between cities along with their distances.

This program provides a simple way to represent and visualize a city transport map using adjacency lists in C++.

8th

This C++ program implements the Optimal Binary Search Tree (OBST) algorithm to construct an optimal binary search tree given the probabilities of successful and unsuccessful searches for each key. Here's how the program works:

1. **OBST Class:**
   - Manages the entire process of constructing an optimal binary search tree.
   - Contains private member variables to store probabilities of successful searches (`p`), probabilities of unsuccessful searches (`q`), elements from which the OBST is to be built (`a`), weight matrix (`w`), cost matrix (`c`), and root matrix (`r`).
   - Provides public member functions to get input data (`get_data`), build the OBST (`build_OBST`), and build the tree (`build_tree`).

2. **get_data Function:**
   - Takes input from the user, including the number of nodes, elements, probabilities for successful searches (`p`), and probabilities for unsuccessful searches (`q`).

3. **Min_Value Function:**
   - Finds a value in the range `r[i][j-1]` to `r[i+1][j]` such that the cost `c[i][k-1]+c[k][j]` is minimum. It returns the optimal value of `k`.

4. **build_OBST Function:**
   - Builds the tables `w`, `c`, and `r` using the given probabilities.
   - Initializes the matrices for trees with one node and iteratively computes the values for trees with more nodes.

5. **build_tree Function:**
   - Constructs the optimal binary search tree using the tables built by the `build_OBST` function.
   - Uses a queue to traverse the `r` matrix and print the nodes, left child, and right child of each node.

6. **Main Function:**
   - Creates an instance of the `OBST` class.
   - Calls the `get_data` function to get input from the user.
   - Calls the `build_OBST` function to construct the OBST.
   - Calls the `build_tree` function to build and display the optimal binary search tree.

### Example Execution:
```
Optimal Binary Search Tree

Enter the number of nodes: 4
Enter the data as...
a[1]: 1
a[2]: 2
a[3]: 3
a[4]: 4

Enter probabilities for successful search ...
p[1]: 3
p[2]: 3
p[3]: 1
p[4]: 1

Enter probabilities for unsuccessful search ...
q[0]: 2
q[1]: 3
q[2]: 1
q[3]: 1
q[4]: 1

The Optimal Binary Search Tree For the Given Node Is...
The Root of this OBST is ::2
The Cost of this OBST is::32

        NODE    LEFT CHILD      RIGHT CHILD
         2               1       3
         1
         3                       4
         4
```

This output shows the optimal binary search tree constructed for the given probabilities and elements. Each node is shown with its left and right children.

10th

This C++ program implements a class `hp` that performs operations on two separate heaps. Here's a breakdown of how it works:

1. **hp Class:**
   - Manages two heaps, one for storing maximum values and another for storing minimum values.
   - Contains private member variables `heap` and `heap1` to store the elements of the heaps, along with `n1` (the number of elements) and `i` (used for iteration).

2. **Constructor:**
   - Initializes the heap arrays by setting their first element to 0.

3. **getdata Function:**
   - Takes input from the user for the number of students (`n1`) and their marks.
   - Inserts each mark into both heaps using the `insert1` and `insert2` functions.

4. **insert1 Function:**
   - Inserts an element into the heap for maximum values (`heap`).
   - Adjusts the heap structure by calling the `upadjust1` function.

5. **upadjust1 Function:**
   - Performs upward adjustment in the max-heap to maintain the heap property.
   - Swaps the element with its parent until the heap property is restored.

6. **insert2 Function:**
   - Inserts an element into the heap for minimum values (`heap1`).
   - Adjusts the heap structure by calling the `upadjust2` function.

7. **upadjust2 Function:**
   - Performs upward adjustment in the min-heap to maintain the heap property.
   - Swaps the element with its parent until the heap property is restored.

8. **minmax Function:**
   - Outputs the maximum and minimum marks by accessing the root elements of the max-heap (`heap`) and min-heap (`heap1`), respectively.

9. **Main Function:**
   - Creates an instance of the `hp` class.
   - Calls the `getdata` function to input student marks and populate the heaps.
   - Calls the `minmax` function to display the maximum and minimum marks.

### Example Execution:
```
enter the no. of students : 10
enter the marks : 54 65 25 43 85 95 73 45 21 25
max marks : 95
min marks : 21
```

This output indicates that the maximum mark obtained is 95, and the minimum mark obtained is 21.


12th

This C++ program provides a simple employee management system using file handling. Here's how it works:

1. **Struct Employee:**
   - Represents the structure of an employee with fields like ID, name, designation, and salary.

2. **Function `addEmployee`:**
   - Allows the user to add a new employee to the file.
   - Takes input for employee ID, name, designation, and salary.
   - Writes the employee details to the file using binary file writing.

3. **Function `deleteEmployee`:**
   - Allows the user to delete an employee from the file based on their ID.
   - Creates a temporary file to store non-deleted records.
   - Reads each record from the original file, skips the record with the given ID, and writes the rest to the temporary file.
   - Deletes the original file and renames the temporary file to replace it.

4. **Function `displayEmployee`:**
   - Allows the user to display details of an employee based on their ID.
   - Reads each record from the file and compares the ID with the given ID.
   - If found, displays the details of the employee.

5. **Main Function:**
   - Opens the file (`employee.dat`) in binary mode for both input and output. If the file doesn't exist, it creates a new one.
   - Displays a menu with options to add, delete, or display employee details, and to exit.
   - Based on the user's choice, it calls the corresponding function.
   - The program continues running until the user chooses to exit.

### Example Execution:
```
1. Add Employee
2. Delete Employee
3. Display Employee
4. Exit
Enter your choice: 1
Enter employee ID: 1
Enter employee name: John Doe
Enter employee designation: Manager
Enter employee salary: 50000
Employee added successfully!

1. Add Employee
2. Delete Employee
3. Display Employee
4. Exit
Enter your choice: 3
Enter employee ID to display: 1
Employee ID: 1
Employee Name: John Doe
Employee Designation: Manager
Employee Salary: 50000

1. Add Employee
2. Delete Employee
3. Display Employee
4. Exit
Enter your choice: 2
Enter employee ID to delete: 1
Employee deleted successfully!

1. Add Employee
2. Delete Employee
3. Display Employee
4. Exit
Enter your choice: 3
Enter employee ID to display: 1
Employee not found!

1. Add Employee
2. Delete Employee
3. Display Employee
4. Exit
Enter your choice: 4
Exiting...
``` -->
