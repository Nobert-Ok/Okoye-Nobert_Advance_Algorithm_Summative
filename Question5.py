# importing libraries needed for the problem
from collections import defaultdict
import heapq


edges = [[1,2,24],[1,4,20],[3,1,3],[4,3,12]]

# creating a function to compose the edges into a adjancency map
def compose_graph(edges):
    # building our graph with all the individual edges as keys
    # and values being the edges they're connected to and their weight
    # all stored in a list of tuples
    # eg 1:[(2,24),(4,20)] etc
    graph = {x:[] for x in range(1,len(edges)+1)}
    
    # looping through the edges array and unpacking the variables/
    for a,b,c in edges:
        # a <-----> b
        # since we have undirected connected edges, we map them 
        # according against each other.
        # the content of the values i.e the connecting edge and the weight
        # are stored in tuples
        # eg 1:(2,24)
        if a not in graph or b not in graph:
            # checking for the first occurrence of a and b and storing
            # a as key and (b,c) as value and vice verse for b
            graph[a] = (b,c)
            graph[b] = (a,c)
        else:
            # if we have seen these edges, we then need to add 
            # to what we already have
            graph[a].append((b,c))
            graph[b].append((a,c))

    # returning the graph
    return graph   


# creating a function shortestReach that would take in 
# arguments like the number of edges, the array of edges
# and the starting point
def shortestReach(n,edges,s):
    
    # initailizing the heap and adding the weight  and the starting node 
    heap = [(0, s)]
    
    # calling the function to compose the graph into an adjancency 
    # matrix
    graph = compose_graph(edges)
    
    # initializing a dcitionary that would help keep track of the 
    # shortest reach, we put the edges as the key and infinity 
    # as the value
    answer    = {}
    for a in range(1, n + 1):
        answer[a] = float('inf')
        
    # since we're starting from the s, initialize s to 0 because
    # it connects to itself
    answer[s] = 0
    
    # while the heap is not empty, let's pop out the first 
    # tuple in the heap
    while heap:
        t = heapq.heappop(heap)
        # using a BFS approach, go through that edge
        for h in graph[t[1]]:
            # if the weight of connecting edge is greater than
            # the original weight of the edge plus the current weight
            # set the connecting edge weight to be the sum of the 
            # original weight of the edge plus the current weight
            if answer[h[0]] > answer[t[1]] + h[1]:
                answer[h[0]] = answer[t[1]] + h[1]
                # if the tuple is already in the heap
                # remove them and call the heapify() function on the heap 
                # to sort them accordingly
                if (h[1], h[0]) in heap:
                    heap.remove((h[1], h[0]))
                    heapq.heapify(heap)
                # pushing the current weight and its edge to the heap
                heapq.heappush(heap, (answer[h[0]], h[0]))
      
    # initializing out result array to store the shortest reach  
    shortest_reach = []
    # looping through the dictionary with value as the shortest reach
    # and adding them to array
    for i in answer:
        shortest_reach.append(answer[i])
    # returning an array of with the shortest reach of each edge starting
    # from one
    return shortest_reach[1:]
s = 1
# calling the function
print(shortestReach(len(edges),edges,s))

