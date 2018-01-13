#First frame of video should be static 
#Use first background as base image

import cv2 , time, pandas
from datetime import datetime

#Trigger the camera while the frame is static
#capturing from webcam videocapture has arg 0 
#Gray out the backgorund image and current frame to a gray frame
#Apply the difference between them (delta frame) [between the base background and the current image]
# apply threshold, if pixel below threshold make it white else make it black
#find the contours of the white frame
#check if the area of the countors is more than say 500px, consider the object to be a moving object
#draw a rectangle around countours greater than the minimum area
#detect the time the moving object enteres the video frame and when is exited the the video frame 

#Trigger the webcam 

first_frame = None 
status_list = [None, None] #first value of this list will always be 0
times = []
#throw the times list into a pandas dataframe and then into a csv file
df = pandas.DataFrame(columns = ["Start", "End"])
video = cv2.VideoCapture(0)

#motion - > white ow black
while True:

	check, frame = video.read()
	status = 0


	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#remove noise and increase accuracy using gaussian blur
	#using the standard gaussian kernel 
	gray = cv2.GaussianBlur(gray, (21,21), 0)

	if first_frame is None:
		first_frame = gray #assign grey numpy array of the first frame
		continue 

 
    
    delta_frame = cv2.absdiff(first_frame, gray)

    #return a tuple returning the frame in position 2 
    thresh_frame = cv2.threshold(delta_frame, 30, 255,cv.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 3)
    
    #fidn_contours , store them in a tuple and check their areas
    (_,cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    
    #filter countours
    for contour in cnts:
    	if cv2.contourArea(countour) < 10000:
    		continue
         
        #change status if moving object appears in frame 
        status = 1 
        
    	#if not draw a rectangle aroud the current frame 
    	(x,y,w,h) = cv2.boundingRect(contour)
    	cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0),4)	
    status_list.append(status)

    if status_list[-1] == 1 and status_list[-2] == 0:
    	times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
    	times.append(datetime.now())
    	

	cv2.imshow("Capturing", gray)
	cv2.imshow("Delta Frame", delta frame)
	cv2.imshow("Threshold frame", thresh_frame)
	cv2.imshow("Color Frame", frame)

	key = cv2.waitKey(1)

	if key==ord('q'):
		if status == 1:
			times.append(datetime.now())
		break
	#print(status)

print(status_list)
print(times)	

for i in range(0, len(times), 2):
	df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index = True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows