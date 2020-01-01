"""
analyze.py
====================================
The Analysis Module for Moss
(For info. on how this works contact varshneybhupesh@gmail.com)
"""


class Node:
    """A Single Submitted file"""

    def __init__(self, name):
        self.name = name
        self.tag = None
        self.links = []


class Mgroups:
    """A Disconnected directed graph consisting all individual solutions"""

    linkCount = 0

    def __init__(self):
        self.nodes = []
        self.nodeCount = 0

    def relatesTo(self, P1, P2, node1, node2):
        """Set a path between two file nodes"""
        node_obj_dict = {}

        for r in self.nodes:
            node_obj_dict[r.name] = r

        if node1 in node_obj_dict.keys() and node2 in node_obj_dict.keys():
            if P1 < P2:
                node_obj_dict[node1].links.append(node_obj_dict[node2])
            elif P1 > P2:
                node_obj_dict[node2].links.append(node_obj_dict[node1])
            else:
                node_obj_dict[node1].links.append(node_obj_dict[node2])

        Mgroups.linkCount += 1

    def __indegree(self, node: Node):
        indegree_count = 0
        for n in self.nodes:
            for link in n.links:
                if link.name == node.name:
                    indegree_count += 1
        return indegree_count

    def __outdegree(self, node: Node):
        return len(node.links)

    def set_tags(self):
        """Assign appropriate tag to a Node"""
        for node in self.nodes:
            in_degree = self.__indegree(node)
            out_degree = self.__outdegree(node)

            if in_degree == 0 and out_degree > 0:
                node.tag = "D"
            elif in_degree > 0 and out_degree == 0:
                node.tag = "C"
            elif in_degree != 0 and out_degree != 0:
                node.tag = "DC"

    def createNodes(self, node_set: set):
        """Create multiple nodes at the same time"""
        for n in node_set:
            self.addNode(n)

    def addNode(self, name: str):
        if name not in [r.name for r in self.nodes]:
            node = Node(name)
            self.nodes.append(node)
            self.nodeCount += 1
        return node

    def displayNodes(self):
        return [r.name for r in self.nodes]

    def displayTags(self):
        """Display Nodes with their Tags"""
        for node in self.nodes:
            print("{}, tag = {}".format(node.name, node.tag))

    def d2c(self):
        """All Direct Distributor to Culprit paths"""
        paths = []
        for node in self.nodes:
            for link in node.links:
                if node.tag == "D" and link.tag == "C":
                    paths.append(tuple((node.name, link.name)))
        return paths

    def d2dc(self):
        """All Direct Distributor to potential Distributor-Culprit paths"""
        paths = []
        for node in self.nodes:
            for link in node.links:
                if node.tag == "D" and link.tag == "DC":
                    paths.append(tuple((node.name, link.name)))
        return paths

    def dc2c(self):
        """All potential Distributor-Culprit to direct Culprit paths"""
        paths = []
        for node in self.nodes:
            for link in node.links:
                if node.tag == "DC" and link.tag == "C":
                    paths.append(tuple((node.name, link.name)))
        return paths

    def __repr__(self):
        """Pretty prints the graph"""
        paths = ""
        for node in self.nodes:
            for link in node.links:
                paths += "{0} --> {1}\n".format(node.name, link.name)
        return paths
