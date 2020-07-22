#Finding the dominant colour of the image and compressing the image by representing the image with that colour

#importing libraries
import pandas as pa
import numpy as np
import math as m
import matplotlib.pyplot as mp
import skimage as sk
from skimage.transform import resize 

#importing image
oriimg=sk.io.imread('13.jpg')

#resizing the original image
rel_len=400
n,m,k=oriimg.shape
img=resize(oriimg,(int(rel_len*(n/m)),rel_len))

#difference between original image and resized image
mp.figure(figsize=(15,15))
mp.axis('off')

mp.subplot(121)
mp.title('Original Image')
mp.imshow(oriimg)

mp.subplot(122)
mp.title('Resized Image')
mp.imshow(img)

mp.show()

#shape of new image and flattening it
n,m,l=img.shape  
img.shape=(n*m,l)

#Finding number of clusters
clus=8

#initializing the cluster
centers=np.random.rand(clus,3)

#helper functions

def distance(ar,i):
    #Ecluidian Distance
    return (centers[i][0]-ar[0])**2+(centers[i][1]-ar[1])**2+(centers[i][2]-ar[2])**2

#K-Means
itr=20
for k in range(itr):
    newcenters=np.zeros((clus,3))
    count=np.ones(clus)
    for i in img:
        dist=np.zeros(clus)
        for j in range(clus):
            dist[j]=distance(i,j)
        x=dist.argmin()
        count[x]=count[x]+1
        newcenters[x]=newcenters[x]+i
        
    for i in range(clus):
        centers[i]=newcenters[i]/count[i]

#Dominant colours
print("Dominant colours of image are", clus)
mp.axis('off')
mp.imshow([centers])
mp.show()
                
        
#Generating new image
newimg=[]
for i in img:
    dist=np.zeros(clus)
    
#finding appropriate clusters
    for j in range(clus):
        dist[j]=distance(i,j)
    x=dist.argmin()
    newimg.append(centers[x])

#converting to original shape
newimg=np.array(newimg)
newimg.shape=(n,m,l)
    
#Comparison of images
mp.figure(figsize=(15,15))
mp.axis('off')

mp.subplot(121)
mp.imshow(oriimg)
mp.title('Original Image')

mp.subplot(122)
mp.imshow(newimg)
mp.title('Resultant Image')
    
    
    
    
    
    
    




    









































