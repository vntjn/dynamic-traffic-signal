import math

def GreenTimeFactory(density):
    #Average speed of vehicles crossing the junction
    averageSpeed = 3.3  #in metre/second
    
    #The Average distance these vehicles have to cross
    averageDistance = 20 #in metres
    
    #The Average Time Taken to cross the junction
    yellowTime=averageDistance/averageSpeed
    
    #The Green Time for the stopLght in seconds
    greenTime=[]
    
    for i in density:
        time=math.ceil((126*i) + yellowTime)
        if(time<15):
            greenTime.append(15)
        elif(time>120):
            greenTime.append(120)
        else:
            greenTime.append(time)
    return greenTime
    
#print(GreenTimeFactory([0.5654521994325492, 0.6150901126469405, 0.7156921047289967, 0.2609135636212505]))