import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread('0015561.jpg')

#to display image and take in points
plt.figure()
plt.imshow(img)
plt.show()

#bottom left cordinates
bl_x=292
bl_y=994

#top left cordinates
tl_x=564	
tl_y=763
#top right cordinates
tr_x=804
tr_y=757

#bottom right cordinates 
br_x=1008
br_y=956

#visulization purposes
cv2.circle(img,(bl_x,bl_y),15,(0,255,255),4)
cv2.circle(img,(tl_x,tl_y),15,(0,255,255),4)
cv2.circle(img,(tr_x,tr_y),15,(0,255,255),4)
cv2.circle(img,(br_x,br_y),15,(0,255,255),4)

cv2.line(img,(bl_x,bl_y),(tl_x,tl_y),(0,0,0),3)
cv2.line(img,(tl_x,tl_y),(tr_x,tr_y),(0,0,0),3)
cv2.line(img,(tr_x,tr_y),(br_x,br_y),(0,0,0),3)
cv2.line(img,(br_x,br_y),(bl_x,bl_y),(0,0,0),3)


#image dimensions
h,w,_=img.shape
#store visulaize
cv2.imwrite('points.jpg',img)


#region of intrest in the image
source_points=np.float32([ [bl_x,bl_y],[tl_x,tl_y],[tr_x,tr_y],[br_x,br_y]  ])
#destination points 
destination_points = np.float32([ [0,1700], [0, 0], [300, 0], [300, 1700] ])

#reading the visualized
image=cv2.imread('points.jpg')
#get homography matrix
matrix = cv2.getPerspectiveTransform(source_points, destination_points)
# get the newe image 
result = cv2.warpPerspective(image, matrix, (300,1700))

# show the image on a axis
plt.figure()
plt.imshow(result)
plt.show()
cv2.imwrite("birdie.jpg",result)

# camera matrix
mtx=[[1203.032354,0,720.0],[0,1284.609285,540.0],[0,0,1]] 
#distortion matrix
dist=[ 0 , 0 ,  0,0 ]

#300 pixels correspond to 3.6 meters
ppx=300/3.6
#calculation as per the document
Lh = np.linalg.inv(np.matmul(matrix, mtx))
# getting the ppy
pix_per_meter_y = ppx * np.linalg.norm(Lh[:,0]) / np.linalg.norm(Lh[:,1])
print(ppx, pix_per_meter_y)
#length ahead in meters
length=1700/pix_per_meter_y
print(length)

cv2.waitKey(0)
