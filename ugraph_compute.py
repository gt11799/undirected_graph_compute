#!/usr/bin/env python
'''
some base compute of undirected graph
'''

from collections import deque

#for test
UGRAPH10 = {0:set([]), 1:set([2,3,4]), 2:set([1,3]), 3:set([1,2]), 4:set([1]), 5:set([6]),
         6:set([5]), 7:set([])}

def bfs_visited(ugraph, start_node):
    '''
    Take an undirected graph and a node,
    return the set of all nodes visited.
    '''
    visited = set([start_node])
    tovisit = deque([start_node])
    while tovisit:
        node = tovisit.popleft()
        for item in ugraph[node]:
            if item not in visited:
                visited.add(item)
                tovisit.append(item) 
                
    return visited
    
def cc_visited(ugraph):
    '''
    Take an undirected graph
    return the set of connected components.
    Need the bfs_visited
    '''
    remain_node = ugraph.keys()
    cc_set = []
    while remain_node:
        node = remain_node.pop()
        visited = bfs_visited(ugraph, node)
        cc_set.append(visited)
        remain_node = [item for item in remain_node if item not in visited]
    return cc_set
    
def largest_cc_size(ugraph):
    '''
    Take an undirected graph,
    return the size of the largest connected component.
    Need cc_visited and bfs_visited
    '''
    cc_set = cc_visited(ugraph)
    try:
        return max([len(item) for item in cc_set])
    except(ValueError):
        return 0
        
def compute_resilience(ugraph, attack_order):
    '''
    Take an undirected graph and a list of nodes,
    return the size of the largest connected component for removing the node.
    The list consist of size_origin, size_removed_[0]...
    '''
    result = [largest_cc_size(ugraph)]
    ugraph_attack = dict(ugraph)
    for item in attack_order:
        ugraph_attack.pop(item)
        for node in ugraph_attack:
            try:
                ugraph_attack[node].remove(item)
            except(KeyError):
                pass
        result.append(largest_cc_size(ugraph_attack))
        
    return result
    
    
def test_bfs():
    'test bfs_visited'
    for node in UGRAPH10.keys():
        print("start at: %s, bfs-visted: %s" %(node, bfs_visited(UGRAPH10,node)))
        
def test_cc():
    'test cc_visited, largest_cc_size'
    print("cc-visited: %s" %cc_visited(UGRAPH10))
    print("largest-cc-size: %s" %largest_cc_size(UGRAPH10))
    
def test_resilience():
    'test compute_resilience'
    print("when attack node: %s, the compute_resilience is: %s" \
    %([1,4,5], compute_resilience(UGRAPH10, [1,4,5])))
    
        
if __name__ == '__main__':
    #test_bfs()
    #test_cc()
    test_resilience()
    
