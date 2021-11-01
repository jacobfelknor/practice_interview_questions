# my implementation of a graph data structure


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.visited = False  # for traversal algorithms
        # any other attrs for the node could go here. This is general

    def __repr__(self) -> str:
        return f"Node({self.val})"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, self.__class__):
            return False
        else:
            return self.val == o.val

    def __hash__(self) -> int:
        return hash(self.val)


class DirectedGraph:
    def __init__(self) -> None:
        self.verticies = dict()
        self.visited = set()

    def check_exists(self, *args):
        for node in args:
            if node not in self.verticies:
                raise ValueError(f"Node {node} does not exist in this graph")

    def add_vertex(self, node: Node) -> None:
        if node in self.verticies:
            raise ValueError(f"Node {node} already in graph. Cannot add duplicates")
        else:
            self.verticies[node] = []  # initialize to empty adjacency list

    def remove_vertex(self, node: None) -> None:
        if node not in self.verticies:
            raise ValueError(f"Node {node} does not exist in graph")
        else:
            del self.verticies[node]

    def add_edge(self, from_node: Node, to_node: Node) -> None:
        self.check_exists(from_node, to_node)
        # both nodes are in graph... proceed
        self.verticies[from_node].append(to_node)

    def rm_edge(self, from_node: Node, to_node: Node) -> Node:
        self.check_exists(from_node, to_node)
        # both nodes are in graph... proceed
        self.verticies[from_node].remove(to_node)

    def set_all_unvisited(self) -> None:
        # mark all nodes as univisited
        for node in self.verticies.keys():
            node.visited = False

    def bfs(self, start: Node):
        # just traverse, no searching for now
        self.check_exists(start)
        # starting node is in graph... proceed
        self.visited = set()
        q = []

        q.append(start)
        self.visited.add(start)

        while len(q) > 0:
            # while there are items in queue, visit those nodes
            current = q.pop(0)
            print(current)
            for node in self.verticies[current]:
                # if node in adjacency list hasn't been self.visited, proceed
                if node not in self.visited:
                    self.visited.add(node)
                    q.append(node)

    def _dfs(self, current: Node):
        self.visited.add(current)
        print(current)

        for node in self.verticies[current]:
            if node not in self.visited:
                self._dfs(node)

    def dfs(self, start: Node):
        self.check_exists(start)
        self.visited = set()
        self._dfs(start)

    def __str__(self) -> str:
        return str(self.verticies)


if __name__ == "__main__":
    g = DirectedGraph()
    n1 = Node(1)
    n2 = Node(4)
    n3 = Node(53)
    n4 = Node(3)

    g.add_vertex(n1)
    try:
        g.add_vertex(Node(1))
        assert False
    except ValueError:
        # threw exception as expected
        pass

    g.add_vertex(n2)
    g.add_vertex(n3)

    print(g)

    g.remove_vertex(n2)
    print(g)

    try:
        g.remove_vertex(n4)
        assert False
    except ValueError:
        # threw exception as expected
        g.add_vertex(n4)

    try:
        g.add_edge(n1, n2)
        assert False
    except ValueError:
        # threw exception as expected
        pass

    g.add_vertex(n2)
    g.add_edge(n1, n2)
    g.add_edge(n2, n1)
    print(g)
    g.rm_edge(n2, n1)
    print(g)
    g.add_edge(n2, n1)
    g.add_edge(n2, n3)
    g.add_edge(n1, n4)

    print("BFS:")
    g.bfs(n1)
    print("\nDFS:")
    g.dfs(n1)
