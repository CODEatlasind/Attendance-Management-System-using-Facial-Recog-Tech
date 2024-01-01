cap=cv.VideoCapture(0)

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
