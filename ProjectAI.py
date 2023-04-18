import random

roomtemp= random.randint(10,30)

while(True):
    print(roomtemp)
    print("The Temperature controller has been turned on.")
    print("Enter the temperature to set:")
    settemp=int(input())
    while(roomtemp!=settemp):
        if(settemp>roomtemp):
                roomtemp+=1
        elif(settemp<roomtemp):
                roomtemp-=1
                
    print("Room temperature has been set to required temp.Try to maintain this temperature.")
    print("TO turn off the temperature controller press E.")
    key=input()
    if(key == 'e'or key == 'E'):
        exit();
        
        