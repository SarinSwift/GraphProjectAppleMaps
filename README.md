## Graph Theory Application -- Apple Map Routes

Check out my [Medium Article](https://medium.com/@sarinyaswift/graph-implementation-a8277c6a2ad9)!

#### Things to know about graphs  

**Parts of a graph**
1. Vertices(nodes) - This is where the actual data gets stored.
2. Edges(connections) - Connects 2 different vertices together. Additionally, these edges can have weights.

**Types of graphs**
1. Undirected - Vertices on both sides of the edges have connection to each other and you can see that the relationship goes both ways.
2. Directed - This allows only one vertex to have a relationship with another vertex. We can tell it's a directed graph if there are arrows pointed on the edge.

**Properties of a graph**
These properties define the graph itself, and is not a specific drawing of the graph. Here are some examples of graph properties.
1. Path - A sequence of vertices where they are adjacent to the vertex next to it.
2. Coloring - An assignment of different colors to all vertices so the vertex at the end of each edge has a unique color.
3. Degree - The number of edges that point out of the vertex
4. Weight - Weighted graphs are graphs which it's edges have weights/values.
5. Diameter - The longest shortest path of that graph
6. Connected graph - When a graph has at least 1 vertex and there is a path between all vertices.

**Problems that can be solved**  
Here are some examples that can be questioned/solved in a graph model
1. Verification - Do these vertices form a path?
2. Existence - Is there a path in this graph?, Is there a path of length 5?
3. Instance - Find a path from source vertex to distance vertex.
4. Enumeration - How many paths of length 3 exists in this graph?
5. Optimization - What is the longest path?, What is the shortest path?

#### Graph Algorithms
**Breadth First Search (BFS)**   
BFS is a way to traverse through the graph in an order where it's closest to the root vertex. In an iterative approach, we use a Queue data structure to keep track of each step in the traversals.   
Representation of running BFS on a graph starting at vertex D. Note that we are choosing the neighbor based on its alphabetical order.  
[…Image of graph and list of order called on BFS…]  
Graph problems that can be solved using the BFS algorithm:
- Finding a path from a vertex to another
- Finding the minimum path from a vertex to another
- Finding all the paths from a vertex to another
- Finding a minimum spanning tree of an unweighted graph

**Depth First Search (DFS)**  
DFS is a way to traverse through the graph in a way where it tries to go farthest from the root vertex. DFS requires to use a Stack data structure so we go furthest away from the vertex instead of a level search like the bfs algorithm.
Representation of running DFS on a graph starting at vertex G. Note that we are choosing the neighbor based on its alphabetical order.
[…Image of graph and list of order called on DFS…]
Graph problems that can be solved using the DFS algorithm: 
- Proving that a graph is connected
- Finding if there are existing paths within the graph
- Checking if a graph is bipartite (A graph is bipartite when the vertices can be divided into 2 independent sets and all the edges from one of the set connect to the other. Or we can also say a bipartite graph will not contain any odd length cycles.)

**Prim's Algorithm**  
Prim's algorithm is a greedy algorithm that finds a minimum spanning tree in a weighted undirected graph. The algorithm builds up a tree one vertex at a time choosing it's minimal weight of a vertex in each step.

**Dijkstra's Algorithm**  
Dijkstra's algorithm is another greedy algorithm that that finds the shortest path between vertices in a graph. The algorithm finds the shortest path between the given vertex and every other connecting vertex to it. We can also optimize the run time of this algorithm by using a priority queue. This reduces the time of looking up the vertex that has the least distance.
