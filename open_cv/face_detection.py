#an xml file contains features of a face
#basically pixel intensity samples
#using alot of data -> haarcasades
#load image in python and search the entire
#image using the xml file
import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#using greyscale increases accuracy
img = cv2.imread("news.jpg")

#find coordinates of the starting face 
#giving the height and width of the face
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)
for x, y , w , h in faces:
	img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),3)
cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()