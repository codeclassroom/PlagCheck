class Mgroup:

    linkCount = 0

    class Node:

        def __init__(self, name):
            self.name = name
            self.perc = []
            self.links = []
            self.visited = False

        def addEdge(self, P1, P2, node):
            if P1 < P2:
                self.tag = "D"
                node.tag = "C"
            elif P1 > P2:
                self.tag = "C"
                node.tag = "D"
            else:
                self.tag = "DC"
                node.tag = "DC"

            self.perc.append(P1)
            node.perc.append(P2)
            self.links.append(node)
            Mgroup.linkCount += 1

    def __init__(self):
        self.nodes = []
        self.nodeCount = 0

    def addNode(self, name: str):
        if name not in self.nodes:
            node = self.Node(name)
            self.nodes.append(node)
            self.nodeCount += 1
        return node

    def allNodes(self):
        return [r.name for r in self.nodes]

    def d2c(self):
        # All Direct Distributor to Culprit paths
        paths = []
        for node in self.nodes:
            for link in node.links:
                if node.tag == "D" and link.tag == "C":
                    paths.append(tuple((node.name, link.name)))
        return paths

    def d2dc(self):
        # All Direct Distributor to potential Distributor-Culprit paths
        paths = []
        for node in self.nodes:
            for link in node.links:
                if node.tag == "D" and link.tag == "DC":
                    paths.append(tuple((node.name, link.name)))
        return paths

    def dc2c(self):
        # All potential Distributor-Culprit to direct Culprit paths
        paths = []
        for node in self.nodes:
            for link in node.links:
                if node.tag == "DC" and link.tag == "C":
                    paths.append(tuple((node.name, link.name)))
        return paths

    def __repr__(self):
        paths = ""
        for node in self.nodes:
            for link in node.links:
                paths += "{0} --> {1}\n".format(node.name, link.name)
        return paths
