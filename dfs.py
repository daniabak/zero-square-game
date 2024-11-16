from functions import getNextState
from collections import deque

def dfsSolving(currentState):
    stack = deque()
    visitedList = []
    stack.append(currentState)
    while stack:
        currentPop = stack.pop()
        if currentPop.grid not in [state.grid for state in visitedList]:
            visitedList.append(currentPop)
        nextStateList = getNextState(currentPop)
        for nextState in nextStateList:
            if nextState.grid not in [state.grid for state in visitedList]:
                nextState.parent = currentPop
                visitedList.append(nextState)
                stack.append(nextState)
        if currentPop.checkWin():
            path = []
            while currentPop:
                path.append(currentPop)
                currentPop = currentPop.parent
            path.reverse()
            for i in path:
                i.print_patch()
            print("visited list length:", len(visitedList))
            print("path length:", len(path))
            print("_________finished DFS_______")
            break

# Example usage
# dfsSolving(initial_state)
