from functions import getNextState,extractMovingCellFromGrid
from collections import deque
import time
import sys
def dfsSolving(currentState):
    start_time=time.time()
    queue = deque([])
    visitedSet = set()  
    queue.append(currentState)
    
    while queue:
        currentPop = queue.pop()
        
        grid_tuple = tuple(tuple(row) for row in currentPop.grid)
        
        if (grid_tuple,tuple(extractMovingCellFromGrid(currentPop.grid))) not in visitedSet:
            visitedSet.add((grid_tuple,tuple(extractMovingCellFromGrid(currentPop.grid))))
        else:
            continue
        
        nextStateList = getNextState(currentPop)
        for nextState in nextStateList:
            next_grid_tuple = tuple(tuple(row) for row in nextState.grid)
            if (next_grid_tuple,tuple(extractMovingCellFromGrid(nextState.grid))) not in visitedSet:
                nextState.parent = currentPop  
                queue.append(nextState)
        
        if currentPop.checkWin():
            path = []
            while currentPop is not None:
                path.append(currentPop)
                currentPop = currentPop.parent
            path.reverse()
            for state in path:
                state.print_patch()
            
            end_time=time.time()
            print("Dfs:\nvisited set length:", len(visitedSet),)
            print("path length:", len(path),"\nspace:",sys.getsizeof(queue)+sys.getsizeof(visitedSet)," bytes")
            print(f"\ntime:,{end_time-start_time} seconds")
            print("_________finished DFS_______")
            break
