import cv2

import pathlib
import os

def DensityFactory(time=1,cam=1):
    
    #Extracting CWD to create filepath
    path=pathlib.Path(__file__).parent.absolute()
    path=str(path)
    cam=str(cam)
    
    #determining the time of day
    timePeriod=''
    if (time==1):
        timePeriod='morning'
        
    elif (time==2):
        timePeriod='dusk'
        
    else :
        timePeriod='night'
        
    #Create filePath to Main average and extract its dimensions
    avgMainName= 'AverageMain' + cam + '.jpg'
    avgMainPath=os.path.join(path,'AverageMain',timePeriod,avgMainName)
    avgMain=cv2.imread(avgMainPath)
    
    #Read the daily average to use as background
    avgDailyName= 'AverageDaily' + cam + '.jpg'
    avgDailyPath=os.path.join(path,'AverageDaily',timePeriod,avgDailyName)
    avgDaily=cv2.imread(avgDailyPath)
    
    #Raed the current Frame to extract density
    currFrameName= 'CurrentFrame' + cam + '.jpg'
    currFramePath=os.path.join(path,'CurrentFrame',timePeriod,currFrameName)
    currFrame=cv2.imread(currFramePath)
    
    #resize Current Frame to fit the size of matrices
    height,width=avgMain.shape[0:2]
    currFrame=cv2.resize(currFrame, (width, height), fx=1, fy=1)
    
    #Extracting Frames of interest from the Current Frame
    ls=[]
    if(cam=='1'):
        ls=[0,265,268,658]
    
    elif(cam=='2'):
        ls=[230,420,262,675]
        
    elif(cam=='3'):
        ls=[0,233,30,398]
        
    else:
        ls=[239,478,251,740]
    
    currFrame=currFrame[ls[0]:ls[1] , ls[2]:ls[3]]
    #cv2.imshow("cropped",currFrame)
    
    #convert the images to grayscale
    avgDailyGray= cv2.cvtColor(avgDaily, cv2.COLOR_BGR2GRAY)
    currFrameGray= cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    
    #apply background subtraction to detect foreground objects
    diff=cv2.subtract(avgDailyGray,currFrameGray)
    
    #apply denoising function to the detected foreground
    diff2=cv2.fastNlMeansDenoising(diff,h=10)
    diff3=cv2.fastNlMeansDenoising(diff2,h=10)
    
    #convert the Gray Scale image to b/w image by using threshold function 
    ret,thresh = cv2.threshold(diff3,50,200, cv2.THRESH_BINARY)
    
    #counting the number of white pixels in the image
    #This gives us an estimate of the amount of cars present at the signal
    count=cv2.countNonZero(thresh)
    #cv2.imshow("b/w",thresh)
    #calculating density of cars
    height, width = diff3.shape
    size = diff3.size
    density= float (count/size)
    
    '''
    print ("height and width of the image : ",height, width)
    print ("size of the image in number of pixels : ", size)
    print("The number of computed white pixels are as follows : ",count)
    print("The density of white pixels is : ",density)

    # plot the binary image
    cv2.imshow("normal",currFrame)
    cv2.imshow('bw',thresh)
    
    '''

    return density
    #destroy all windows and free up space
    #cap.release()
    #cv2.destroyAllWindows()
    
#Calling The Density Factory
#print(DensityFactory(1,3))
