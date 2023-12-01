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
        graph = self.graph
        isp = self.isp

        

     
        
        list_clients = self.info["list_clients"]
    
        
        bandwidths = self.info["bandwidths"]
                 

        
        for clients in list_clients[::-1]:
            new_path = []
            final_path = []
            visited_lst = {clients: 1}
            pq = [(0, [clients])]
            nodes_at_zero = {}
            while pq:
                tuple = heapq.heappop(pq)
                d = tuple[0]
                path = tuple[1] 
                
                visited_lst[path[d]] = 1
                
                
                
               
             
                for neighbor in graph[path[d]]:
                  
                    new_path = []
                    if neighbor == isp:
                      final_path = path
                      final_path.append(neighbor)
                      pq = []
                      
                      break
                    
                    if visited_lst.get(neighbor,0) == 0 and bandwidths[neighbor] != 0:
                     
                        new_path = path.copy()
                          
                            
                        new_path.append(neighbor)
                        new_d = d + 1
                    
                        heapq.heappush(pq,(new_d, new_path))
                   

                       
            
                
            for i in final_path:
                    
                if(i != clients):
                    bandwidths[i] = bandwidths[i] - 1
                    if bandwidths[i] == 0:
                        bandwidths[i] = 69

            paths[clients] = final_path[::-1]
           
          
                    
            






        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
       

        return (paths, bandwidths, priorities)