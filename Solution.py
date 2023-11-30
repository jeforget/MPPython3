from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

    def output_paths(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """
        paths, bandwidths, priorities = {}, {}, {}

        #Start by creating the pque
        #The pque will be a priority queue that is ordered by 
        #Try just running bfs, then checking the paths and chnaging the bandwidth based on that.
        paths = bfs_path(self.graph,self.isp,self.info["list_clients"])

        #The tolerance for bandwidth, i.e. the limit at which we start increasing the bandwidth of a node
        bandwidth_tol = 0

        #A map that maps the # of each node for every path
        #Will keep track of how many packets are at each node at a time
        band_map = {}

        return (paths, bandwidths, priorities)
