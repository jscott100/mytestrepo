

import math

import numpy as np

# Ford-Fulkerson algorithm

class Edge(object):

    def __init__(self, u, v, w):
        self.source = u
        self.target = v
        self.capacity = w

    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.target, self.capacity)

class FlowNetwork(object):

    def __init__(self):
        self.adj = {}
        self.flow = {}


    def AddVertex(self, vertex):
        self.adj[vertex] = []

    def GetEdges(self, v):
        return self.adj[v]


print("hello")
