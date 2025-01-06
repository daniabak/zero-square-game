from functions import getNextState,hurestic
import time

def hillClimbing (current):
 start_time=time.time()
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
     end_time=time.time()
 
     print("number of visited states",counter,)
     print(f"\ntime:,{end_time-start_time} seconds")
     break   