#computure vision is based on analyzing images 
#use python to load images and process them 
#computer vision with python using opencv
import cv2
img = cv2.imread("galaxy.jpg",0)
resized = cv2.resize(img,(int(img.shape)[1]/2, int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized)
cv2.imwrite("Galaxy_Resized.jpg", resized)
cv2.waitKey(2000)
cv2.destroyAllWindows()