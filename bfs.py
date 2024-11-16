from functions import getNextState
from collections import deque
def bfsSolving(currentState):
  queue = deque([])
  visitedList=[]
  queue.appendleft(currentState)
  while queue  :
    currentPop=queue.pop()
    if currentPop.grid not in [state.grid for state in visitedList]: 
      visitedList.append(currentPop)
    nextStateList=getNextState(currentPop)
    for nextState in nextStateList:
     if nextState.grid not in [state.grid for state in visitedList]:
        nextState.parent = currentPop  
        queue.appendleft(nextState)  
 
    if currentPop.checkWin():
     path=[]
     while currentPop!=None :
      path.append(currentPop)
      currentPop= currentPop.parent
     path.reverse() 
     for i in path:
      i.print_patch()
     print("visited list length ",len(visitedList ),)
     print("path length:",len(path))
     print("_________finished BFS_______")
     break
    #عم طالع من الكيو وضيفها عالفيست مع شرط وعم جيب النيكست وعم ضيفها عالكيو مع شرط 