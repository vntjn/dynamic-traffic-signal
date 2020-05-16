import DensityFactory
import datetime
import random

def DensityFactoryProduct(cameras):
    time= datetime.datetime.now()
    time.hour
    hour=12
    #minute=time.minute
    minute=30
    density=[]
    densityRand=[]
    
    for i in cameras:
        if hour in range(0,18):
            if (hour==17 and minute in range(30,60)):
                density.append(DensityFactory.DensityFactory(2,i)) #(time, camera)
                #print("dusk")
            else:
                density.append(DensityFactory.DensityFactory(1,i))
                #print("morning")
        elif hour in range(18,24):
            if (hour==18 and minute in range(0,30)):
                density.append(DensityFactory.DensityFactory(2,i))
                #print("dusk")
            else:
                density.append(DensityFactory.DensityFactory(3,i))
                #print("night")
                
    for i in cameras:
        densityRand.append(random.random())
        
    return densityRand
    
#print(DensityFactoryProduct([1,3,4]))