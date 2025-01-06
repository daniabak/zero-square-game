import heapq
from functions import getNextState,hurestic
import time
import sys
def aStar (current):
 start_time=time.time()
 heap=[]
 heapq.heapify(heap)
 visitedList=[]
 visitedList.append(current)
 heapq.heappush(heap,((current.cost +hurestic(current)),current))
 print("hurestic",hurestic(current))
 while heap:
  
  _, popedState=heapq.heappop(heap)
  if popedState.checkWin():
     path=[]
     while popedState!=None :
      path.append(popedState)
      popedState= popedState.parent
     path.reverse() 
     for i in path:
      i.print_patch()
      end_time=time.time()
     print("BFS:\nvisited set length:", len(visitedList),)
     print("path length:", len(path),"\nspace:",sys.getsizeof(heap)+sys.getsizeof(visitedList)," bytes")
     print(f"\ntime:,{end_time-start_time} seconds")
 
     break 
  if popedState.grid not in [state.grid for state in visitedList]:
    visitedList.append(popedState)
  nextStates=getNextState(popedState)
  for next in nextStates:
    g_n=next.cost+popedState.cost
    nexthurestic=hurestic(next)
    f_n=g_n+ nexthurestic
    if next.grid not in [state.grid for state in visitedList] or g_n< next.cost:
        next.parent = popedState 
        next.cost=g_n
        heapq.heappush(heap,(f_n,next))