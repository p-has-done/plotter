class Setting:
    pass


class TemporalSetting(Setting):
    pass


class SpatialSetting(Setting):
    pass


class TemporalSettingTree:
    class TemporalSettingTreeNode:
        def __init__(self, parent, name):
            # initial attributes
            self.parent = parent
            self.name = name
            self.children = list()

            # register as a new child
            parent.children.append(self)


        def isRoot(self):
            return self.parent is None


        def isTerminal(self):
            return len(self.children) == 0


        def getNextSibling(self):
            idx = self.parent.children.index(self)
            return self.parent.children[idx + 1]


        def getNextTerminal(self):
            curr = self
            while curr is self or not curr.isTerminal():
                try:
                    curr = curr.getNextSibling()
                except IndexError:
                    curr = curr.parent
                    if curr.isRoot():
                        raise IndexError
            return curr
    
    
    def __init__(self, root_name):
        self.root_node = self.TemporalSettingTreeNode(None, root_name)
    
    
    def getFirstTerminal(self):
        curr = self.root_node
        while not curr.isTerminal():
            curr = curr.children[0]


class SpatialSettingGraph:
    class SpatialSettingGraphNode:
        def __init__(self, name):
            self.name = name
            self.adj = set()
    
    class SpatialSettingGraphLink:
        def __init__(self, start, end, weight):
            self.start = start
            self.end = end
            self.weight = weight
    
    def __init__(self):
        self.nodes = set()


    def addNode(self, name):
        node = self.SpatialSettingGraphNode(name)
        self.nodes.add(node)
    

    def linkVertex(self, start, end, weight):
        link = self.SpatialSettingGraphLink(start, end, weight)
        start.adj.add(link)
    
    def linkVertex2(self, start, end, weight):
        self.linkVertex(self, start, end, weight)
        self.linkVertex(self, end, start, weight)
