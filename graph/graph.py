class Queue:
    def __init__(self, items):
        self.items = items
    
    def load(self, item):
        self.items.append(item)
    
    def unload(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None
    
    def len(self):
        return len(self.items)

class Stack:
    def __init__(self, items):
        self.items = items
    
    def load(self, item):
        self.items.append(item)
    
    def unload(self):
        if self.items:
            return self.items.pop()
        else:
            return None
    
    def len(self):
        return len(self.items)
        
edges = [
    (0,2), (0,3), (0,8),
    (2,3),
    (3,1), (3,2), (3,5), (3,9),
    (4,0), (4,6), (4,8),
    (5,7),
    (6,3)
]

class Node:
    def __init__(self, id):
        self.id = id
        self.previous = None
        self.distance = 0
        self.children = set()
        self.parents = set()
    
    def addchild(self, child):
        self.children.add(child)
    def addparent(self, parent):
        self.parents.add(parent)
    def getchildren(self):
        return list(self.children.copy())
    def getparents(self):
        return list(self.parents.copy())

         
    
    

class Graph:
    def __init__(self, edges):
        self.edges = edges

        self.nodes = {}
        for edge in edges:
            origin = Node(edge[0])
            end = Node(edge[1])
            if origin.id not in self.nodes:
                self.nodes[origin.id] = origin
            if end.id not in self.nodes:
                self.node[end.id] = end
        
        for edge in edges:
            originid = edge[0]
            endid = edge[1]
            self.nodes[originid].addchild(endid)
            self.nodes[endid].addparent(originid)
        
    

    
    def node(self, id):
        return self.nodes[id]

    # def get_dict(self):
    #     return self.dict.copy()
    
    # def get_reversed_dict(self):
    #     return self.reversed_dict.copy()

    def get_ids_breadth_first(self, root):
        queue = Queue([root])
        visited = {root: True}
        traversal = []

        while queue.len() != 0:
            node = self.nodes[queue.unload()]
            traversal.append(node.id)
            for child in node.getchildren():
                if child not in visited:
                    queue.load(child)
                    visited[child] = True
        return traversal


    def get_ids_depth_first(self, node):
        stack = Stack([node])
        visited = {node: True}
        traversal = []

        while stack.len() != 0:
            node = stack.unload()
            traversal.append(node)
            children = self.get_children(node)
            for child in children:
                if child not in visited:
                    stack.load(child)
                    visited[child] = True
        return traversal
    
    def set_distance_and_previous(self, root):
        queue = Queue([root])
        visited = {root: True}
        root.distance = 0
        root.previous = None

        while queue.len() != 0:
            node = queue.unload()
            children = self.get_children(node)
            for child in children:
                if child not in visited:
                    queue.load(child)
                    visited[child] = True
                    child.distance = node.distance + 1
                    child.previous = node
    
    def calc_distance(self, origin, end):
        self.set_distance_and_previous(origin)
        return self.dict[end].distance
    
    def shortest_path(self, origin, end):
        self.set_distance_and_previous(origin)
        path = []
        current_node = end

g = Graph(edges)
print(g.get_dict())
print(g.get_children(3))
print(g.get_parents(3))
print(g.get_ids_breadth_first(4))
print(g.get_ids_depth_first(4))

edges2 = [
    (0,1), (1,2), (2,3), (3,0)
]
g2 = Graph(edges2)
print(g2.get_dict())
print(g2.get_ids_breadth_first(0))
print(g2.get_ids_depth_first(0))


edges3 = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4)
]
g3 = Graph(edges3)
print(g3.get_dict())
print(g3.get_ids_breadth_first(0))

print(g3.get_ids_breadth_first(4))

edges4 = []
for i in range(1):
    edges4.append((i, i+1))
g4 = Graph(edges4)
print(g4.get_dict())
print(g4.get_ids_breadth_first(0))

