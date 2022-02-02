import random
import numpy as np
import matplotlib
from collections import deque

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

# Global Queue
global queue

'''
BFS add to queue 
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    global queue
    if initialize:
        queue = deque()

    queue.append((node_id, parent_node_id))
    return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    # Your code here
    global queue
    # if(len(queue) == 0):
    #     return True
    # else:
    #     return False
    if not queue:
        return True
    else:
        return False

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    global queue
    (node_id, parent_node_id) = queue.popleft()
    return (node_id, parent_node_id)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    global queue
    if initialize:
        queue = deque()

    queue.append((node_id, parent_node_id))
    return

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    # Your code here
    global queue
    # if(len(queue) == 0):
    #     return True
    # else:
    #     return False
    if not queue:
        return True
    else:
        return False

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    global queue
    (node_id, parent_node_id) = queue.pop()
    return (node_id, parent_node_id)

'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    global queue
    if(initialize == True):
        queue = []
        queue.append((node_id, parent_node_id, cost))
    else:
        i = 0
        while(i < len(queue) and cost >= queue[i][2]):
            i += 1
        queue.insert(i, (node_id, parent_node_id, cost))
    return

'''
UC add to queue 
'''
def is_queue_empty_UC():
    # Your code here
    global queue
    if(len(queue) == 0):
        return True
    else:
        return False

'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    global queue
    (node_id, parent_node_id, cost) = queue.pop(0)
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    global queue
    if(initialize == True):
        queue = []
        queue.append((node_id, parent_node_id, cost))
    else:
        i = 0
        while(i < len(queue) and cost >= queue[i][2]):
            i += 1
        queue.insert(i, (node_id, parent_node_id, cost))
    return

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    # Your code here
    global queue
    if(len(queue) == 0):
        return True
    else:
        return False

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    global queue
    (node_id, parent_node_id, cost) = queue.pop(0)
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    # Your code here 
    for i in range(n):
        state.append(random.randint(1,n))
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    # Your code here 
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if(state[i] == state[j] or abs((state[j] - state[i]) / (j - i)) == 1): # same row or same diagonal via slope -1 or 1
                number_attacking_pairs += 1
    
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    # Your code here
    # Compute all possible moves
    # turns = 0
    final_state = state
    final_state_score = comp_att_pairs(state)

    best_neighbor_state = final_state
    best_neighbor_score = final_state_score
    
    while True:
        # Compute all possible moves and get best one, state is something like [1,3,3,6,8,9,7,8]
        for i in range(len(state)):
            for j in range(1,len(state)+1):
                if(state[i] == j): #not modifying anything
                    continue
                else:
                    neighbor = final_state[0:i] + [j] + final_state[i+1:len(state)]
                    neighbor_score = comp_att_pairs(neighbor)
                    if(neighbor_score < best_neighbor_score):
                        best_neighbor_score = neighbor_score
                        best_neighbor_state = neighbor

        # Update Final State
        if(best_neighbor_score >= final_state_score):
            # print(turns)
            return final_state
        else:
            # Update final_state if best neighbor has a smaller score
            final_state = best_neighbor_state
            final_state_score = best_neighbor_score
            # turns += 1

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):

    final_state = hill_descending(get_rand_st(n), comp_att_pairs)
    while(comp_att_pairs(final_state) != 0):
        final_state = hill_descending(get_rand_st(n), comp_att_pairs)
    # Your code here
    return final_state






