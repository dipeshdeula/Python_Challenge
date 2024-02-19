#open cv in python running a web cam
#open cv helps to interact with webcamp
#scrolling by motion object 

# import cv2
# import numpy as np

# #capturing the video
# cap = cv2.VideoCapture(0)

# blue_lower=np.array([22,93,0])
# blue_upper=np.array([45,167,89])
# prev_y=0

# while True:
#    #give display size for video
#    ret, frame = cap.read()
#    #gray frame vision
#    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    # cv2.imshow('frame',gray)
#    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#    mask=cv2.inRange(hsv, blue_lower, blue_upper)
#    controus,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#    for c in controus:
#       area=cv2.contourArea(c)
#       if area>300:
#          x,y,w,h= cv2.boundingRect(c)
#          cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),2)
#          if y <prev_y:
#             print("Moving down")
#          prev_y=y

#    cv2.imshow('frame',frame)
#    cv2.imshow('mask',mask)

#    #terminate video processing with q
#    if cv2.waitKey(10) == ord ('q'):
#       break
       
# cap.release()
# cv2.destroyAllWindows()
