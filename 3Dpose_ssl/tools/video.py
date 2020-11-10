import cv2 
video_full_path="SGM1.avi" 
cap = cv2.VideoCapture(video_full_path) 
print cap.isOpened() 
frame_count = 1 
success = True 
while(success): 
 success, frame = cap.read() 
 #print 'Read a new frame: ', success 
 y = 368.0/frame.shape[0]
 x = 368.0/frame.shape[1]
 #print x,y
 resized = cv2.resize(frame, None, fx=x, fy=y)
 params = [] 
 #params.append(cv.CV_IMWRITE_PXM_BINARY) 
 params.append(1) 
 cv2.imwrite("result/" + "%d.jpg" % frame_count, resized, params) 
 
 frame_count = frame_count + 5
 
cap.release() 