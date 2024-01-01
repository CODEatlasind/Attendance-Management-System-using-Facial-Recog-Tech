import cv2 as cv
import os
import time
import uuid

#path for all images

image_PATH=os.path.join("images")
os.makedirs(image_PATH)

#setting number of images to be generated
number_images=15

#set pesron name as diectory name
p_name=input("ENTER the name of person :")
if(p_name)
p_path = os.path.join(image_PATH, p_name)

os.makedirs(p_path)


#capture images
# cap=cv.VideoCapture(0)

# for imgnum in range(number_images):
#     print("Collecting Images {}".format(imgnum))
#     ret,frame=cap.read()
#     imgname=os.path.join(p_path,f'{str(uuid.uuid1())}.jpg')
#     cv.imwrite(imgname,frame)
#     cv.imshow('frame',frame)
#     time.sleep(5)
    
#     if(cv.waitKey(1) & 0xFF==ord('q')):
#         break
# cap.release()
# cv.destroyAllWindows()

