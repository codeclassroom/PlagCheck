class Node:
    """A Single Sdubmitted file"""

    def __init__(self, name):
        self.name = name
        self.perc = []
        self.tag = None
        self.links = []


class Mgroups:
    """A directed graph consisting all individual solutions"""

    linkCount = 0

    def __init__(self):
        self.nodes = []
        self.nodeCount = 0

    def relatesTo(self, P1, P2, node1, node2):
        node_dict = {}

        for r in self.nodes:
            node_dict[r.name] = r

        if node1 in node_dict.keys() and node2 in node_dict.keys():
            if P1 < P2 and (node_dict[node1].tag and node_dict[node2].tag not in ["D", "C"]):
                node_dict[node1].tag = "D"
                node_dict[node2].tag = "C"
                node_dict[node1].links.append(node_dict[node2])
            elif P1 > P2:
                node_dict[node1].tag = "C"
                node_dict[node2].tag = "D"
                node_dict[node2].links.append(node_dict[node1])
            else:
                node_dict[node1].tag = "DC"
                node_dict[node2].tag = "DC"
                node_dict[node1].links.append(node_dict[node2])

        node_dict[node1].perc.append(P1)
        node_dict[node2].perc.append(P2)
        Mgroups.linkCount += 1

    def createNodes(self, node_set: set):
        for n in node_set:
            self.addNode(n)

    def addNode(self, name: str):
        if name not in [r.name for r in self.nodes]:
            node = Node(name)
            self.nodes.append(node)
            self.nodeCount += 1
        return node

    def allNodes(self):
        return [r.name for r in self.nodes]

    def displayTags(self):
        for node in self.nodes:
            print("{}, tag = {}".format(node.name, node.tag))

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


# mg = Mgroups()
# mg.createNodes({'1', '2', '3', '4', '5', '6', '7'})

# mg.relatesTo(45, 88, '3', '1')
# mg.relatesTo(46, 90, '3', '2')
# mg.relatesTo(34, 64, '3', '4')
# mg.relatesTo(34, 64, '3', '5')
# mg.relatesTo(64, 66, '4', '2')
# mg.relatesTo(64, 66, '5', '2')
# mg.relatesTo(94, 94, '4', '5')
# mg.relatesTo(33, 61, '7', '6')

# print(mg)
# print(mg.allNodes())
# print("D to C paths\n", mg.d2c())
# print("D to DC paths\n", mg.d2dc())
# print("DC to C paths\n", mg.dc2c())
