class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end, _ in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            new_paths = self.get_paths(node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
        return paths 

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            new_path = self.get_shortest_path(node, end, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path
        return shortest_path

    def print_paths(self):
        return self.graph_dict

if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris", 10),
        ("Mumbai", "Dubai", 15),
        ("Paris", "Dubai", 11), 
        ("Paris", "New York", 9),
        ("Dubai", "New York", 22), 
        ("New York", "Toronto", 6)
    ]
    
    route_graph = Graph(routes)
    
    # paths = route_graph.print_paths()
    # print(paths)

    # data = route_graph.get_paths("Mumbai", "New York")
    # print(data)

    data = route_graph.get_shortest_path("Mumbai", "New York")
    print(data)