class Mgroup:

    linkCount = 0

    class Node:

        def __init__(self, name, perc):
            self.name = name
            self.perc = perc
            self.links = []
            self.visited = False

        def addEdge(self, node):
            if self.perc < node.perc:
                self.tag = "D"
                node.tag = "C"
            elif self.perc > node.perc:
                self.tag = "C"
                node.tag = "D"
            else:
                self.tag = "DC"
                node.tag = "DC"

            self.links.append(node)
            Mgroup.linkCount += 1

    def __init__(self):
        self.nodes = []
        self.nodeCount = 0

    def addNode(self, data: dict):
        if data not in self.nodes:
            node = self.Node(data['name'], data['perc'])
            self.nodes.append(node)
            self.nodeCount += 1
        return node

    def allNodes(self):
        for node in self.nodes:
            print(node.name, "tag: ", node.tag)

    def __repr__(self):
        result = ""
        for node in self.nodes:
            for link in node.links:
                result += "{0} --> {1}\n".format(node.name, link.name)
        return result


mg = Mgroup()
n0 = mg.addNode({'name': 'A', 'perc': 45})
n1 = mg.addNode({'name': 'B', 'perc': 50})
n2 = mg.addNode({'name': 'C', 'perc': 34})

n0.addEdge(n1)
n1.addEdge(n2)
n2.addEdge(n0)

print(mg)
mg.allNodes()
