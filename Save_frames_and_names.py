import cv2

vidcap = cv2.VideoCapture('val.mp4')
success,image = vidcap.read()
digit1=0
success = True


while success:
    digit=str(digit1)
    digit=digit.zfill(4)

    success,image = vidcap.read()
    
    cv2.imwrite("%s.jpg" % digit, image)          # save frame as JPEG file 
    print(digit+" yuklendi")
   
    digit1 += 1