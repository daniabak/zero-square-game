from functions import getNextState,hurestic
import time
import sys
def steapestHillClimbing (current):
 start_time=time.time()
 counter=1
 minHuris=hurestic(current)
 minState=current
 while True:
  
  if current.checkWin() :
    end_time=time.time()
       
    print(f"\ntime:,{end_time-start_time} seconds")
    print("get win,counter is ",counter)
    break
  nextStates=getNextState(current)
  for next in nextStates:
    huNext=hurestic(next)
    if huNext<minHuris:
     minHuris=huNext
     minState=next
  if minHuris<hurestic(current):
    counter+=1
    current=minState

  else :
     
     print("stopped ,counter is ",counter)
     break    