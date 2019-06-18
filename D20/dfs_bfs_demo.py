#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Here we define a graph structure
the neighbour of A is B and C
the neighbour of B is A, C and D
the neighbour of C is A, B, D and E
this is a undirected graph
'''
graph = {
    'A':['B', 'C'],
    'B':['A', 'C', 'D'],
    'C':['A', 'B', 'D', 'E'],
    'D':['B', 'C', 'E', 'F'],
    'E':['C', 'D'],
    'F':['D']
}

def BFS(graph, vertex):
    # use queue as the structure
    queue = []
    # add the first node into the queue
    queue.append(vertex)
    # use a set to store all visited node
    looked = set()
    # add the first node into the set
    looked.add(vertex)
    # if the queue is not empty, search
    while len(queue) > 0:
        # get a node from the head and check all its neighbours
        temp = queue.pop(0)
        nodes = graph[temp]
        # Get all its neighbouring
        for w in nodes:
            # judge if it is looked
            if w not in looked:
                # if not looked, ass to the queue, and add to the looked set
                queue.append(w)
                looked.add(w)
        print(temp, end=' ')

def DFS(graph, vertex):
    # use stack as the structure
    stack = []
    # add the first element
    stack.append(vertex)
    # use a set to store all visited node
    looked = set()
    # add the first node into the set
    looked.add(vertex)
    # if the stack is not empty, search
    while len(stack) > 0:
        # get a node from the tail and check all its neighbours
        temp = stack.pop()
        nodes = graph[temp]
        # Get all its neighbouring
        for w in nodes:
            # judge if it is looked
            if w not in looked:
                stack.append(w)
                looked.add(w)
        print(temp, end=' ')

def main():
    print('BFS', end=' ')
    BFS(graph, 'A')
    print()
    print('DFS', end=' ')
    DFS(graph, 'A')
    print()


if __name__ == "__main__":
    main()
