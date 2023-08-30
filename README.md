# Description
 - This repo has been created for individual training purpose 
 - The bolts and nuts displayed in the video are detected with the developed software. (YoloV8 was preferred for modelling.)  
 - The bounding boxes are drawn around these detections. 
 - Each detection is tracked, counted and marked upon the object in the flowing frames.  
 
 # Run
  - This project has been prepared on colab and is ready to work. Open the StromaVision.ipynb file on colab and select the “run all” option.  
 
 # Libraries
  
  - torch
  - numpy as np
  -	cv2
  -	ultralytics
  -	supervision
  -	ByteTrack
  
  # Extras
  
  - check_frame.py  file was created by me to check for corruption on the annotations files.
  - Save_frames_and_names.py file was created by me to convert and rename frames to image files.
  - There is the Train_Results folder where the training results are analyzed.
  - There are 2 Turkish explanation files that contain my working method, the problems I encountered and my solutions.
  - There is a output.mp4  file as output example


 

