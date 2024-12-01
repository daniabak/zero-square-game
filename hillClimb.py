import heapq
from functions import getNextState,hurestic
def hillClimbing (current):
 counter=1
 while True:
  
  if current.checkWin() :
    break
  huClim=hurestic(current)
  nextStates=getNextState(current)
  nexthurestic=hurestic(nextStates[0])
  if nexthurestic<huClim:
    counter+=1
    current=nextStates[0]
  else :
     break  