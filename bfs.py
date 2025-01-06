from functions import getNextState,extractMovingCellFromGrid
from collections import deque
from patch import directionLogs
import time
import sys
    # عم طالع من الكيو وضيفها عالفيست مع شرط وعم جيب النيكست وعم ضيفها عالكيو مع شرط 
def bfsSolving(currentState):
    start_time=time.time()
    queue = deque([])
    visitedSet = set()  
    queue.appendleft(currentState)
    
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
                queue.appendleft(nextState)
        
        if currentPop.checkWin():
            path = []
            while currentPop is not None:
                path.append(currentPop)
                currentPop = currentPop.parent
            path.reverse()
            for state in path:
                state.print_patch()
            end_time=time.time()
            print("BFS:\nvisited set length:", len(visitedSet),)
            print("path length:", len(path),"\nspace:",sys.getsizeof(queue)+sys.getsizeof(visitedSet)," bytes")
            print(f"\ntime:,{end_time-start_time} seconds")
            print("_________finished BFS_______")
            break
