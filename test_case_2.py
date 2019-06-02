import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread('0018705.jpg')

plt.figure()
plt.imshow(img)
plt.show()

cv2.circle(img,(427,991),15,(0,0,255))
cv2.circle(img,(663,699),15,(0,255,0))
cv2.circle(img,(748,699),15,(0,255,255))
cv2.circle(img,(1116,991),15,(0,0,0))

cv2.line(img,(427,991),(663,699),(0,0,0),3)
cv2.line(img,(663,699),(748,699),(0,0,0),3)
cv2.line(img,(748,701),(1116,991),(0,0,0),3)
cv2.line(img,(1116,991),(427,991),(0,0,0),3)

h,w,_=img.shape
cv2.imwrite('points2.jpg',img)

source_points=np.float32([ [427,991],[663,699],[748,699],[1116,991]  ])
destination_points = np.float32([ [0,1700], [0, 0], [300, 0], [500, 1700] ])


image=cv2.imread('points2.jpg')
matrix = cv2.getPerspectiveTransform(source_points, destination_points)
result = cv2.warpPerspective(image, matrix, (400,1700))
plt.figure()
plt.imshow(result)
plt.show()
cv2.imwrite("birdie_test_case_2.jpg",result)

mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]] 
dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]

ppx=300/3.6
print(ppx)
Lh = np.linalg.inv(np.matmul(matrix, mtx))
pix_per_meter_y = ppx * np.linalg.norm(Lh[:,0]) / np.linalg.norm(Lh[:,1])
print(ppx, pix_per_meter_y)
length=1700/pix_per_meter_y
print(length)




cv2.waitKey(0)
