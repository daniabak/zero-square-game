import heapq
from functions import getNextState
import time
import sys
def ucs_solving (current):
 start_time=time.time()
 heap=[]
 heapq.heapify(heap)
 visitedList=[]
 visitedList.append(current)
 heapq.heappush(heap,(current.cost,current))
 while heap:
  
  popedState=heapq.heappop(heap)
  if popedState[1].checkWin():
     path=[]
    #خزنتها بمتحول مشان ماعدل عالتيوب  
     popedStateFromTuple=popedState[1]
     while popedStateFromTuple!=None :
      path.append(popedStateFromTuple)
      popedStateFromTuple= popedStateFromTuple.parent
     path.reverse() 
     for i in path:
      i.print_patch()
      end_time=time.time()
     print("UCS:\nvisited set length:", len(visitedList),)
     print("path length:", len(path),"\nspace:",sys.getsizeof(heap)+sys.getsizeof(visitedList)," bytes")
     print(f"\ntime:,{end_time-start_time} seconds")
     break 
  if popedState[1].grid not in [state.grid for state in visitedList]:
    visitedList.append(popedState[1])
  nextStates=getNextState(popedState[1])
  for next in nextStates:
    next.cost=popedState[1].cost+1
    if next.grid not in [state.grid for state in visitedList]:
        next.parent = popedState[1] 
        heapq.heappush(heap,(next.cost,next))