from functions import getNextState
from collections import deque

def dfsRecusionSolving(currentState):
    visitedList = []

    while True:
        visitedList.append(currentState)
        nextStateList = getNextState(currentState)
        for nextState in nextStateList:
            if nextState.grid not in [state.grid for state in visitedList]:
                nextState.parent = currentState
                dfsRecusionSolving(nextState)
            if currentState==None  :  
                 dfsRecusionSolving(nextState.parent)
            if currentState.checkWin():
               
               path = []
               while currentState:
                   path.append(currentState)
                   currentState = currentState.parent
               path.reverse()
               for i in path:
                   i.print_patch()
               print("visited list length:", len(visitedList))
               print("path length:", len(path))
               print("_________finished DFS_______")
               break

