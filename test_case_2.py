import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread('0018768.jpg')

plt.figure()
plt.imshow(img)
plt.show()

cv2.circle(img,(412,985),15,(0,0,255))
cv2.circle(img,(588,777),15,(0,255,0))
cv2.circle(img,(848,777),15,(0,255,255))
cv2.circle(img,(1116,985),15,(0,0,0))

cv2.line(img,(412,985),(588,777),(0,0,0),3)
cv2.line(img,(848,777),(588,777),(0,0,0),3)
cv2.line(img,(848,777),(1116,985),(0,0,0),3)
cv2.line(img,(1116,991),(412,985),(0,0,0),3)

h,w,_=img.shape
cv2.imwrite('points2.jpg',img)

source_points=np.float32([ [412,985],[588,777],[848,777],[1116,985]  ])
destination_points = np.float32([ [0,1700], [0, 0], [300, 0], [300, 1700] ])


image=cv2.imread('points2.jpg')
matrix = cv2.getPerspectiveTransform(source_points, destination_points)
result = cv2.warpPerspective(image, matrix, (300,1700))
plt.figure()
plt.imshow(result)
plt.show()
cv2.imwrite("birdie_test_case_2.jpg",result)

#mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]] 
#dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]

mtx=[[1203.032354,0,720.0],[0,1284.609285,540.0],[0,0,1]] 
dist=[ 0 , 0 ,  0,0 ]



ppx=300/3.6
print(ppx)
Lh = np.linalg.inv(np.matmul(matrix, mtx))
pix_per_meter_y = ppx * np.linalg.norm(Lh[:,0]) / np.linalg.norm(Lh[:,1])
print(ppx, pix_per_meter_y)
length=1700/pix_per_meter_y
print(length)




cv2.waitKey(0)
