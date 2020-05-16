import cv2
from PIL import Image

import numpy as np

import pathlib
import os

#global loop to limit number of recurrences
loop=0
def AverageDailyFactory(time=1, cam=1):
    
    #Extracting CWD to create filepath
    path=pathlib.Path(__file__).parent.absolute()
    path=str(path)
    cam=str(cam)
    videoDailyName= cam + 'camera7.mp4'
    
    #Creating filepath of video and opening the Video file
    videoPath=os.path.join(path,'VideoDaily',videoDailyName)
    cap= cv2.VideoCapture(videoPath)
    
    #applying image averaging filter
    imlist=[]
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break    
        imlist.append(frame)
        i+=1
    w,h=Image.fromarray(imlist[0],mode='RGB').size
    N=len(imlist)

    # Create a numpy array of floats to store the average (assume RGB images)
    arr=np.zeros((h,w,3),np.float)

    # Build up average pixel intensities
    for im in imlist:
        imarr=np.array(Image.fromarray(im),dtype=np.float)
        arr=arr+imarr/N

    # Round values in array and cast as 8-bit integer
    arr=np.array(np.round(arr),dtype=np.uint8)
    
    #Convert numpy array to Image
    avgDaily = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
    
    #determining the time of day
    timePeriod=''
    if (time==1):
        timePeriod='morning'
        
    elif (time==2):
        timePeriod='dusk'
        
    else :
        timePeriod='night'
        
    #picking up main average according to time of day   
    avgMainName= 'AverageMain' + cam + '.jpg'
    avgMainPath=os.path.join(path,'AverageMain',timePeriod,avgMainName)
    avgMain=cv2.imread(avgMainPath)
    
    #Extracting Frames of interest from the images
    ls=[]
    if(cam=='1'):
        ls=[0,265,268,658]
    
    elif(cam=='2'):
        ls=[230,420,262,675]
        
    elif(cam=='3'):
        ls=[0,233,30,398]
        
    else:
        ls=[239,478,251,740]
    
    avgMain=avgMain[ls[0]:ls[1] , ls[2]:ls[3]]
    avgDaily=avgDaily[ls[0]:ls[1] , ls[2]:ls[3]]
    
    #convert the images to grayscale
    avgMainGray= cv2.cvtColor(avgMain, cv2.COLOR_BGR2GRAY)
    avgDailyGray= cv2.cvtColor(avgDaily, cv2.COLOR_BGR2GRAY)

    #apply background subtraction to detect the difference between average images
    diff=cv2.subtract(avgMainGray,avgDailyGray)

    #apply denoising function to the detected foreground
    diff2=cv2.fastNlMeansDenoising(diff,h=10)
    diff3=cv2.fastNlMeansDenoising(diff2,h=10)
    
    #convert the Gray Scale image to b/w image by using threshold function 
    ret,thresh = cv2.threshold(diff3,50,200, cv2.THRESH_BINARY)

    #counting the number of white pixels in the image
    #to compare the background images
    count=cv2.countNonZero(thresh)
    print(" The number of computed white pixels are as follows : ",count)
    
    
    #comapring the two average images and reiterating function 
    #if differences are found
    global loop
    if(count > 100 and loop < 3):
        loop += 1
        print("Iteration:",loop)
        AverageDailyFactory()

    #storing the daily average to location
    else:
        avgDailyName= 'AverageDaily' + cam + '.jpg'
        avgDailyPath=os.path.join(path,'AverageDaily',timePeriod,avgDailyName)
        cv2.imwrite(avgDailyPath,avgDaily)

#Calling The Daily Average Factory
AverageDailyFactory(1,3)
