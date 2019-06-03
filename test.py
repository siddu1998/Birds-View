import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread('0015561.jpg')

#to display image and take in points
plt.figure()
plt.imshow(img)
plt.show()


bl_x=int(input('please enter bottom left x'))
bl_y=int(input('please enter bottom left y'))

tl_x=int(input('please enter top left x'))
tl_y=int(input('please enter top left y'))

tr_x=int(input('please enter top right x'))
tr_y=int(input('please enter top right y'))

br_x=int(input('please enter bottom right x'))
br_y=int(('please enter bottom right y'))

#
cv2.circle(img,(bl_x,bl_y),15,(0,255,255),4)
cv2.circle(img,(tl_x,tl_y),15,(0,255,255),4)
cv2.circle(img,(tr_x,tr_y),15,(0,255,255),4)
cv2.circle(img,(br_x,br_y),15,(0,255,255),4)

cv2.line(img,(bl_x,bl_y),(tl_x,tl_y),(0,0,0),3)
cv2.line(img,(tl_x,tl_y),(tr_x,tr_y),(0,0,0),3)
cv2.line(img,(tr_x,tr_y),(br_x,br_y),(0,0,0),3)
cv2.line(img,(br_x,br_y),(bl_x,bl_y),(0,0,0),3)

h,w,_=img.shape
cv2.imwrite('points.jpg',img)

source_points=np.float32([ [bl_x,bl_y],[tl_x,tl_y],[tr_x,tr_y],[br_x,br_y]  ])
destination_points = np.float32([ [0,1700], [0, 0], [300, 0], [300, 1700] ])


image=cv2.imread('points.jpg')
matrix = cv2.getPerspectiveTransform(source_points, destination_points)
result = cv2.warpPerspective(image, matrix, (300,1700))
plt.figure()
plt.imshow(result)
plt.show()
cv2.imwrite("birdie.jpg",result)

mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]] 
dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]

ppx=300/3.6
Lh = np.linalg.inv(np.matmul(matrix, mtx))
pix_per_meter_y = ppx * np.linalg.norm(Lh[:,0]) / np.linalg.norm(Lh[:,1])
print(ppx, pix_per_meter_y)
length=1700/pix_per_meter_y
print(length)




cv2.waitKey(0)