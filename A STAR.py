#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict
H_dist = {}

def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}               # store distance from starting node
    parents = {}         # parents contains an adjacency map of all nodes

    # distance of starting node from itself is zero
    g[start_node] = 0
    # start_node is root node (so parent is itself)
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == None:
            print("Path does not exist!")
            return None

        # if the current node is the stop_node
        # then we begin reconstructing the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        # iterate through neighbors
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        # remove n from open_set and add to closed_set
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None


# define function to return neighbor and its distance from the passed node
def get_neighbors(v):
    """
    Retrieves a value from the Graph_nodes dictionary based on the provided key.

    Parameters:
    v (hashable): The key used to look up the value in the Graph_nodes dictionary.
    Returns:
    The value associated with the key `v` in the Graph_nodes dictionary if the key exists;
    otherwise, returns an empty list.
    """
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return []


def heuristic(n):
    return H_dist[n]


# Input graph and heuristic
graph = defaultdict(list)
n, e = map(int, input().split())
for i in range(e):
    u, v, cost = map(str, input().split())
    t = (v, float(cost))
    graph[u].append(t)
    t1 = (u, float(cost))
    graph[v].append(t1)

# Input heuristics
for i in range(n):
    node, h = map(str, input().split())
    H_dist[node] = float(h)

print("Heuristic values:", H_dist)

Graph_nodes = graph
print("Graph:", graph)

aStarAlgo('S', 'G')
