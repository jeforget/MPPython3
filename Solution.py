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

        #A list of maps that maps the # of each node for every path.
        #Will keep track of how many packets are at each node at a time.
        #index corresponds to step in path, i.e. the isp node should be index 0 (we will ignore this node).
        #the lengnth of this list is probably gonna need to at least be the length of the longest path.
        #to stave time and space only a node that is used will need to be in the map
        band_list = []

        #This list will be populated and once a node has more nodes than bandwidth_tol we increase the bandwidth.
        #Once it goes through all of the paths we return. 

        return (paths, bandwidths, priorities)
