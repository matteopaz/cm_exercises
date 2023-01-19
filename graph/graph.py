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
        self.distance = -1
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
                self.nodes[end.id] = end
        
        for edge in edges:
            originid = edge[0]
            endid = edge[1]
            self.nodes[originid].addchild(endid)
            self.nodes[endid].addparent(originid)
        
    

    
    def node(self, id):
        return self.nodes[id]

    def get_children(self,node):
        return self.nodes[node].getchildren()
    
    def get_parents(self, node):
        return self.nodes[node].getparents()

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
            node = self.nodes[stack.unload()]
            traversal.append(node.id)
            children = node.getchildren()
            for child in children:
                if child not in visited:
                    stack.load(child)
                    visited[child] = True
        return traversal
    
    def set_distance_and_previous(self, root):
        queue = Queue([root])
        visited = {root: True}
        self.nodes[root].distance = 0
        self.nodes[root].previous = None

        for node in self.nodes:
            self.nodes[node].previous = None
            self.nodes[node].distance = -1

        while queue.len() != 0:
            node = self.nodes[queue.unload()]
            for child in node.getchildren():
                if child not in visited:
                    queue.load(child)
                    visited[child] = True
                    self.nodes[child].distance = node.distance + 1
                    self.nodes[child].previous = node.id
    
    def calc_distance(self, origin, end):
        self.set_distance_and_previous(origin)
        return self.nodes[end].distance + 1
    
    def shortest_path(self, origin, end):
        self.set_distance_and_previous(origin)
        path = []
        current_node = self.nodes[end]
        prev = current_node.previous
        while prev != origin:
            if prev == None:
                return False
            path.append(prev)
            current_node = self.nodes[prev]
            prev = current_node.previous
        return [origin] + path[::-1] + [end]

class WeightedGraph:
    def __init__(self, weight_dict):
        self.dict = weight_dict
        self.nodes = {}
        for edge in self.dict: # Appends all nodes
            origin = edge[0]
            end = edge[1]
            self.nodes[origin] = Node(origin)
            self.nodes[end] = Node(end)
        
        for edge in self.dict: # Adds all children and parents
            origin = edge[0]
            end = edge[1]
            self.nodes[origin].addchild(end)
            self.nodes[end].addparent(origin)
        
    
    def calc_distance(self, origin, end):

        visited = {} # children visited, distance must now be fixed
        for nodeid in self.nodes:
            self.nodes[nodeid].distance = 9999999
        self.nodes[origin].distance = 0
        current_node = self.nodes[origin]
        # for n in self.nodes:
        #     print(n, ":", self.nodes[n].getchildren(), ":", self.nodes[n].distance)
        # print("------")
        while end not in visited:
            # for n in self.nodes:
            #     print(n, ":", self.nodes[n].getchildren(), ":", self.nodes[n].distance)
            # print("------")
            for childid in current_node.getchildren():
                child = self.nodes[childid]
                edge = (current_node.id, child.id)
                wt = self.dict[edge]
                child.distance = min(child.distance, current_node.distance + wt)
                # print current node and current node dist and wt
                # print("current node:", current_node.id, "current node dist:", current_node.distance, "wt:", wt)
                # print("child", child.id, "distance", child.distance)

            visited[current_node.id] = True

            min_viewed = {"node": None, "dist": 9999999}
            for node in self.nodes:
                if self.nodes[node].distance <= min_viewed["dist"] and node not in visited:
                    min_viewed["node"] = node
                    min_viewed["dist"] = self.nodes[node].distance
            if min_viewed["node"] == None:
                break
            current_node = self.nodes[min_viewed["node"]]

        return self.nodes[end].distance
    
    def shortest_path(self, origin, end):
        self.calc_distance(origin, end)
        reduced = []
        for edge in self.dict:
            wt = self.dict[edge]
            nodea = self.nodes[edge[0]]
            nodeb = self.nodes[edge[1]]
            if nodea.distance - nodeb.distance == wt:
                reduced.append(edge[::-1])
        unweighted = Graph(reduced)
        # print(unweighted.edges)
        # print(origin, end)
        return unweighted.shortest_path(origin, end)
        
        

weights = {
    (0,1): 3, (1,0): 3,
    (1,7): 4, (7,1): 4,
    (7,2): 2, (2,7): 2,
    (2,5): 1, (5,2): 1,
    (5,6): 8, (6,5): 8,
    (0,3): 2, (3,0): 2,
    (3,2): 6, (2,3): 6,
    (3,4): 1, (4,3): 1,
    (4,8): 8, (8,4): 8,
    (8,0): 4, (0,8): 4
}   

g = WeightedGraph(weights)
print([g.calc_distance(8,n) for n in range(9)])
print(g.shortest_path(8,6))

edges = [
    # make a 3 cycle
    (0,1), (1,2), (2,0),
]
g = Graph(edges)
b = g.get_ids_breadth_first(0)
d = g.get_ids_depth_first(0)
print(b)
print(d)
# edges = [
#     (0, 1), (0,2),
#     (1,3),
#     (2,3), (2,5),
#     (3,1), (3,4),
#     (6,5), (6,7),
#     (7,6), (7,8),
#     (8,9), (8,7),
#     (9,8)
# ]

# g = Graph(edges)


# print(g.calc_distance(0, 4))
# print(g.shortest_path(0, 4))
# edges2 = [
#     (0,1), (1,2), (2,3), (3,0)
# ]
# g2 = Graph(edges2)
# print(g2.get_dict())
# print(g2.get_ids_breadth_first(0))
# print(g2.get_ids_depth_first(0))


# edges3 = [
#     (0,1), (1,2), (2,3), (3,0),
#     (4,5), (5,6), (6,7), (7,4)
# ]
# g3 = Graph(edges3)
# print(g3.get_dict())
# print(g3.get_ids_breadth_first(0))

# print(g3.get_ids_breadth_first(4))

# edges4 = []
# for i in range(1):
#     edges4.append((i, i+1))
# g4 = Graph(edges4)
# print(g4.get_dict())
# print(g4.get_ids_breadth_first(0))

