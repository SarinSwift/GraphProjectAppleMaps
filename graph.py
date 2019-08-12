class Vertex(object):

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.

        name: the value a vertex holds

        neighbors: set of vertices adjacent to self,
        stored in a dictionary like {neighbor_vertex: weight_of_edge_between_the_2_vertices}
        """
        self.name = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return self.name + " adjacent to " + [x.name for x in self.neighbors]

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors

    def get_name(self):
        """Return the name/value of this vertex."""
        return self.name

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        return self.neighbors[vertex]

class Graph:
    vertices = {}   # dictionary for storing all the vertices in a dictionary that looks like: {vertex name: vertex}

    # Vertex Methods

    def add_vertex(self, name):
        '''Create a vertex from the given name and insert it to the list of vertices we have in the graph'''
        new_vert = Vertex(name)
        self.vertices[name] = new_vert
        return new_vert   # return the new vertex object that we inserted to the list

    def get_vertex(self, name):
        """Return the vertex if it exists"""
        if name in self.vertices:
            return self.vertices[name]

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertices.keys()

    # Connection Methods

    def add_edge(self, from_vert, to_vert, weight=0):
        """add connection from 'from_vert' to 'to_vert' with a weight.
        NOTE that both 'from_vert' and 'to_vert' are names of the vertex that we grab the vertex object from our dictionary.
        """
        if from_vert in self.vertices and to_vert in self.vertices:
            self.vertices[from_vert].add_neighbor(self.vertices[to_vert], weight)
            self.vertices[to_vert].add_neighbor(self.vertices[from_vert], weight)

    def shortes_route(self, from_vert, to_vert, weight=0):
        """
        find the shortet route from location a to location b using BFS
        NOTE: both 'from_vert' and 'to_vert' are names of the vertex
        """
        path_found = False
        q = queue.Queue()       # where we perform bfs
        visited = set()            # keeps track of seen vertices
        path = []               # the path of vertices from from_vert to to_vert

        # add in 'from_vert' as a vertex object and then insert it to the qeueu
        curr = self.get_vertex(from_vert)
        curr.parent = None
        q.put(curr)
        visited.add(curr)

        while q:
            curr = q.get()

            if curr.name == to_vert:
                path_found = True
                break

            for neighbor in curr.neighbors:
                if neighbor.name not in visited:
                    q.put(neighbor)
                    visited.add(neighbor)
                    neighbor.parent = curr

        if path_found:
            curr = self.get_vertex(to_vert)
            while curr is not None:
                path.append(curr.name)
                curr = curr.parent
            return path[::-1]
        else:
            print("No available routes from these locations!")


    def print_graph(self):

        print("# Vertices: " + str(len(self.vertices)))

    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertices.values())


# Create Graph

if __name__ == "__main__":
    '''
    Graph Theory Application on-- Apple Map Routes
    Goal: To solve the following problems--
    1. Checking if there is a path from location A to location B
    2. Finding the fastest route from location A to location B
    3. Seeing how many places we can travel to based on our starting location
    '''

    # Create the graph
    g = Graph()

    # Add locations
    g.add_vertex("Hayes Valley")
    g.add_vertex("Nob Hill")
    g.add_vertex("Japan Town")
    g.add_vertex("Golden Gate Park")
    g.add_vertex("Union Square")
    g.add_vertex("Westfield Mall")

    # Add connecting routes with HayesValley
    g.add_edge("Hayes Valley", "Japan Town", 10)
    g.add_edge("Hayes Valley", "Westfield Mall", 25)

    # Add connecting routes with NobHill
    g.add_edge("Nob Hill", "Golden Gate Park", 38)
    g.add_edge("Nob Hill", "Japan Town", 31)
    g.add_edge("Nob Hill", "Westfield Mall", 27)
    g.add_edge("Nob Hill", "Union Square", 24)

    # Add connecting routes with JapanTown
    g.add_edge("Japan Town", "Hayes Valley", 10)
    g.add_edge("Japan Town", "Nob Hill", 31)
    g.add_edge("Japan Town", "Golden Gate Park", 30)

    # Add connecting routes with UnionSquare
    g.add_edge("Union Square", "Nob Hill", 24)
    g.add_edge("Union Square", "Westfield Mall", 12)


    # print("finding path")
    # print(g.find_path(g.vert_list["Sarin"], g.vert_list["AAA"]))

    # Output the vertices & edges
    # vertices:
    print("The vertices are: ", g.get_vertices())

    # edges:
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_name(), w.get_name()))
