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

    def d2c(self):
        result = ""
        for node in self.nodes:
            for link in node.links:
                if node.tag == "D" and link.tag == "C":
                    result += "{0} --> {1}\n".format(node.name, link.name)
        return result

    def d2dc(self):
        result = ""
        for node in self.nodes:
            for link in node.links:
                if node.tag == "D" and link.tag == "DC":
                    result += "{0} --> {1}\n".format(node.name, link.name)
        return result

    def dc2c(self):
        result = ""
        for node in self.nodes:
            for link in node.links:
                if node.tag == "DC" and link.tag == "C":
                    result += "{0} --> {1}\n".format(node.name, link.name)
        return result

    def __repr__(self):
        result = ""
        for node in self.nodes:
            for link in node.links:
                result += "{0} --> {1}\n".format(node.name, link.name)
        return result


mg = Mgroup()
n0 = mg.addNode({'name': 'A', 'perc': 36})
n1 = mg.addNode({'name': 'B', 'perc': 50})
n2 = mg.addNode({'name': 'C', 'perc': 74})

n0.addEdge(n1)
n0.addEdge(n2)


print(mg)
print("D to C paths\n", mg.d2c())
print("D to DC paths\n", mg.d2dc())
# mg.allNodes()
