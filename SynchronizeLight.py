import turtle

import DensityFactoryProduct
import CreateTrafficLight
import GreenTimeFactory

#The data structures to be used in the project are as follows:

#to store the references to the turtle objects
animationIdDict={}
#to store the densities of the stoplights
densityDict={}
#to store the timer results of the stoplight
timerDict={}
#to check how many times a signal has been red
redCountDict={}
#to allow for the long avaited stoplights to open
redCountQueue=[]
#to set the number of stoplights and the type of junction
lightNumber=[1,2,3,4]

#to store the current state of the flowing stoplight
greenLightTimer=15
greenLightNumber=0

#function to identify the stoplight with the corresponding property
def getNumber(dictList,val): 
    for key, value in dictList.items(): 
         if val == value: 
             return key 
 
#to access the red stops
def redCountAdd(number):
    for i in redCountDict.keys():
        if i==number:
            redCountDict[i]=0
        else:
            redCountDict[i] += 1
    for key, value in redCountDict.items():
        if value >= 4:
            redCountQueue.append(key)

#opening a turtle screen
turtle.TurtleScreen._RUNNING=True
turtle.Screen().setup(width=1.0, height=1.0, startx=None, starty=None)

#time.sleep(12)

#creating the animated stoplights
if(len(lightNumber)==4):
    animationIdList=[CreateTrafficLight.CreateTrafficLight(150,150),CreateTrafficLight.CreateTrafficLight(-150,150),CreateTrafficLight.CreateTrafficLight(150,-150),CreateTrafficLight.CreateTrafficLight(-150,-150)]
elif(len(lightNumber)==3):
    animationIdList=[CreateTrafficLight.CreateTrafficLight(150,150),CreateTrafficLight.CreateTrafficLight(-150,150),CreateTrafficLight.CreateTrafficLight(0,-150)]
animationIdDict=dict(zip(lightNumber,animationIdList))

#initializing all stoplights to stop
for i in lightNumber:
    animationIdDict[i].changeColor("red")

redCountDict={i:0 for i in lightNumber}

#extracting the initial density of all junctions to start the signal
densityList=DensityFactoryProduct.DensityFactoryProduct(lightNumber)
densityDict=dict(zip(lightNumber,densityList))

#computing the initial Timers to compare among them
timerList=GreenTimeFactory.GreenTimeFactory(densityList)
timerDict=dict(zip(lightNumber,timerList))

#displaying the density on the animated stoplights
for i in densityDict.keys():
    animationIdDict[i].printDensity(densityDict[i])

#extracting the appropriate timer time to minimize the density of the junction
greenLightTimer=max(timerDict.values())
greenLightNumber=getNumber(timerDict,greenLightTimer)

#opening the signal with the maximum likelyhood to reduce the traffic on the junction
animationIdDict[greenLightNumber].changeColor("green")

#updating the redCount Matrix according to the decision of the current instance
redCountAdd(greenLightNumber)

#displaying the statistics of the current junction instance
'''
print(greenLightTimer)
print(greenLightNumber)
print(densityDict)
print(timerDict)
print(redCountDict)
print(lightNumber)
print()
print()
'''

#initiating the countdown to allow traffic flow at the stoplight
animationIdDict[greenLightNumber].countdown(greenLightTimer)

#clearing the displayed densities for the next instance
for i in densityDict.keys():
    animationIdDict[i].clearDensity()

#the modified list for holding the new stoplight instances
modLightNumber=[]
RCFlag=0

while True:
    #change the current green stoplight to yellow
    animationIdDict[greenLightNumber].changeColor("yellow")
    
    #create modified list for holding the new stoplight instances
    for i in lightNumber:
        if(i==greenLightNumber):
            continue
        modLightNumber.append(i)
    
    #extracting the initial density of all junctions to start the signal
    densityList=DensityFactoryProduct.DensityFactoryProduct(modLightNumber)
    densityDict=dict(zip(modLightNumber,densityList))
    
    #computing the initial Timers to compare among them
    timerList=GreenTimeFactory.GreenTimeFactory(densityList)
    timerDict=dict(zip(modLightNumber,timerList))
    
    #closing the signal with the maximum likelyhood to prepare for the next instance
    animationIdDict[greenLightNumber].changeColor("red")
    
    #displaying the density on the animated stoplights
    for i in densityDict.keys():
        animationIdDict[i].printDensity(densityDict[i])
    
    #print elements of the redCount Queue before they are modified
    #print(redCountQueue)
    
    #checking if any of the signals have raised a Red Count Exception
    if not redCountQueue:
        #extracting the appropriate timer time to minimize the density of the junction
        greenLightTimer=max(timerDict.values())
        greenLightNumber=getNumber(timerDict,greenLightTimer)
        
        RCFlag=0

    #if they have raised the exception then changing the state of those signals regardless of their density
    else:
        greenLightNumber=redCountQueue[0]
        greenLightTimer=15
        
        #displaying the Red Count Exception
        print("redCountQueue Exception. Other signal will be opened")
        CreateTrafficLight.CreateTrafficLight.printRCException()
        
        #Clearing the redCountQueue for the next instance
        redCountQueue.clear()
        
        RCFlag=1
        
    #opening the signal with the maximum likelyhood to reduce the traffic on the junction
    animationIdDict[greenLightNumber].changeColor("green")
    
    #updating the redCount Matrix according to the decision of the current instance
    redCountAdd(greenLightNumber)
    
    #initiating the countdown to allow traffic flow at the stoplight
    animationIdDict[greenLightNumber].countdown(greenLightTimer)
    
    #clearing the displayed Red Count Exception
    if(RCFlag):
        CreateTrafficLight.CreateTrafficLight.clearRCException()

    #clearing the displayed densities for the next instance
    for i in densityDict.keys():
        animationIdDict[i].clearDensity() 

    #displaying the statistics of the current junction instance   
    '''
    print(modLightNumber)
    print(densityDict)
    print(timerDict)
    print(greenLightTimer)
    print(greenLightNumber)
    print(redCountDict)
    print()
    print()
    '''
    
    #reinitializing the modified list to be able to hold new instances
    modLightNumber.clear()