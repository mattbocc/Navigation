from collections import defaultdict
from typing import List
from queue import PriorityQueue
import heapq
import sys
    


def printDFS(graph, destination, reached):

    p = reached[destination].split()
    p.reverse()                         #reverse list to normal pathing direction
    total = 0
                               
    for i, elem in enumerate(p):
        if i < len(p) - 1:
            current_dist = graph[elem][p[i+1]]
            print(elem + " to " + p[i+1] +": " + current_dist + " mi") #outputting each path with their respective weights
            total += int(current_dist) #adding to total distance

    print("\nTotal Distance: " + str(total) + " mi")


def DFS(graph, origin, destination): 

    if origin == destination: #special case, dest == start
        print("Destination is the same as starting point, 0 mi will be traversed")
        exit()


    frontier = []               #hold our frontier
    frontier.append(origin)
    reached = defaultdict()     #hold our path to every node reached
    reached[origin] = origin


    while len(frontier) > 0:
        parent = frontier.pop()             #popping the node we're traversing from the frontier
        for child in graph[parent]:
            if child == destination:
                reached[child] = str(child) + " " + str(reached[parent])    #add the last step in path to reached
                #print(reached)
                printDFS(graph, destination, reached)
                exit()
            elif child not in reached:      #if the successor child does not have a path yet, add a key and it's path to reached
                reached[child] = str(child) + " " + str(reached[parent])    #add the next step in the path to reached
                frontier.insert(len(frontier), child)
    
    print("Distance: infinity")
    print("Path: None")




def printBFS(graph, destination, reached):

    p = reached[destination].split()
    p.reverse()                         #reverse list to normal pathing direction
    total = 0
                               
    for i, elem in enumerate(p):
        if i < len(p) - 1:
            current_dist = graph[elem][p[i+1]]
            print(elem + " to " + p[i+1] +": " + current_dist + " mi") #outputting each path with their respective weights
            total += int(current_dist)

    print("\nTotal Distance: " + str(total) + " mi")

            
        
        

def BFS(graph, origin, destination):

    if origin == destination: #special case, dest == start
        print("Destination is the same as starting point, 0 mi will be traversed")
        exit()


    frontier = []                   #hold our frontier
    frontier.append(origin)
    reached = defaultdict()         #hold our path to every node reached
    reached[origin] = origin
    solution = False

    while len(frontier) > 0:
        parent = frontier.pop(0)                #popping the node we're traversing from the frontier
        for child in graph[parent]:
            if child == destination:
                reached[child] = str(child) + " " + str(reached[parent])    #add the last step in path to reached
                #print(reached)
                printBFS(graph, destination, reached)
                exit()
            elif child not in reached: #if the successor child does not have a path yet, add a key and it's path to reached
                reached[child] = str(child) + " " + str(reached[parent])    #add the next step in the path to reached
                frontier.append(child)
                #print(frontier)

    print("Distance: infinity")
    print("Path: None")

def printUCS(graph, reached, path, dest): #also used to print Astar

    p = reached[dest].split()
    p.reverse()                             #reverse list to normal pathing direction
    for i, elem in enumerate(p):
        if i < len(p) - 1:
            current_dist = graph[elem][p[i+1]]
            print(elem + " to " + p[i+1] +": " + current_dist + " mi") #outputting each path with their respective weights
    print("\nTotal Distance: " + str(path[dest]) + " mi")

def UCS(graph, origin, destination):

    if origin == destination: #special case, dest == start
        print("Destination is the same as starting point, 0 mi will be traversed")
        exit()

    frontier = PriorityQueue()
    frontier.put((0, origin))
    reached = defaultdict()
    reached[origin] = origin
    totalPath = defaultdict()
    totalPath[origin] = 0
    solution = False


    while frontier.qsize() > 0:                                 #verifying the que has items
        #print(origin in reached)  
        parent = frontier.get()
        #print(frontier.qsize())                                #(0, origin)
        for child in graph[parent[1]]:                          #1st iter graph[origin]
            s = graph[parent[1]][child]                         #value of path
            #print(s)                         
            tot = int(s) + int(parent[0])                       #path total to be stored
            #print(tot)
            if child not in reached:            #check if the child is already reached or if it is see if this pack is shorter
                reached[child] = str(child) + " " + str(reached[parent[1]]) #path follow by current node 
                totalPath[child] = tot
                #print(child)
                #print("\n")
                #print(reached[child])                              
                frontier.put((tot, child))
                if child == destination:
                    solution = True         #let us know a solution exists
            elif child in totalPath:
                if int(tot) < int(totalPath[child]):
                    reached[child] = str(child) + " " + str(reached[parent[1]]) #path follow by current node 
                    totalPath[child] = tot                                      #add the new path total with new key
                    #print(child)
                    #print("\n")
                    #print(reached[child])                              
                    frontier.put((tot, child))                                  #add to the frontier
                    if child == destination and tot < solution:                 #if child is the dest and tot < sol
                        solution = True 
    if solution:
        printUCS(graph, reached, totalPath, destination)
    else:
        print("Distance: infinity")
        print("Path: None")
              


    
def Astar(graph, heuristic, origin, destination):

    if origin == destination: #special case, dest == start
        print("Destination is the same as starting point, 0 mi will be traversed")
        exit()


    frontier = PriorityQueue()
    frontier.put((0, origin))
    reached = defaultdict()
    reached[origin] = origin
    totalPath = defaultdict()
    totalPath[origin] = 0
    solution = False


    while frontier.qsize() > 0:                                 #verifying the que has items
        parent = frontier.get()
        #print(frontier.qsize())                                #(0, origin)
        for child in graph[parent[1]]:                          #1st iter graph[origin]
            s = graph[parent[1]][child]                         #value of path   
            h = int(s) + int(parent[0]) + int(heuristic[child]) #creating the child's new frontier value which includes the heuristic to add to the frontier                
            tot = h - int(heuristic[parent[1]])                 #child total to be stored in totalPath, not including heuristic
            #print(heuristic[child])
            h = tot + int(heuristic[child])
            #print(tot)
            if child not in reached:            #check if the child is already reached or if it is see if this pack is shorter
                reached[child] = str(child) + " " + str(reached[parent[1]]) #path follow by current node 
                totalPath[child] = tot
                #print(child)
                #print("\n")
                #print(reached[child])                              
                frontier.put((h, child))
                if child == destination:
                    solution = True #let us know a solution exists
            elif child in totalPath:
                if int(tot) < int(totalPath[child]):
                    reached[child] = str(child) + " " + str(reached[parent[1]]) #path follow by current node 
                    totalPath[child] = tot
                    #print(child)
                    #print("\n")
                    #print(reached[child])                              
                    frontier.put((tot, child))
                    if child == destination and tot < solution: #add to the frontier
                        solution = True #let us know a solution exists

    if solution: #if a solution exists, print it, if not let the user know
        printUCS(graph, reached, totalPath, destination) #use the same printing as UCS
    else:
        print("Distance: infinity")
        print("Path: None")

    

   
algor = sys.argv[1]
fileOne = sys.argv[2]
origin = sys.argv[3]
destination = sys.argv[4]

#turning heuristic file into list
partial_h = [] 
if (len(sys.argv) > 5):
    fileTwo = sys.argv[5]
    for line in open(fileTwo, "r").readlines():
        strip = line.strip()
        line = strip.split()
        partial_h.append(line)
#print(partial_h) 

#turning input file into list
partial_graph = []    
for line in open(fileOne, "r").readlines():
    strip = line.strip()
    line = strip.split()
    partial_graph.append(line)   
   
#creating a set for vertices to help with graph creation
vertices = set()
for node in partial_graph:
    if node[0].lower() != "end":
        if node[0] not in vertices:
            vertices.add(node[0])
        if node[1] not in vertices:
            vertices.add(node[1])

#creating heuristic dict
heuristic = defaultdict(dict)
for node1 in vertices:
    for node2 in partial_h:
        if node2[0].lower() == "end":
            break
        elif node1 == node2[0]:
            heuristic[node1] = node2[1]
#print(heuristic)

#creating graph dict
graph = defaultdict(dict)
for node1 in vertices:
    for node2 in partial_graph:
        if node2[0].lower() == "end":
            break
        elif node1 == node2[0]:
            graph[node1][node2[1]] = node2[2]
        elif node1 == node2[1]:
            graph[node1][node2[0]] = node2[2]
#print(graph)


        
if(algor.lower() == "dfs"):
    DFS(graph, origin, destination)
elif(algor.lower() == "bfs"):
    BFS(graph, origin, destination)
elif(algor.lower() == "ucs"):
    UCS(graph, origin, destination)
elif(algor.lower() == "astar"):
    Astar(graph, heuristic, origin, destination)
else:
    print("We cannot solve for " + algor.lower() + " Check algorithm spelling and try again (either dfs, bfs, ucs or astar)")
    exit()



    