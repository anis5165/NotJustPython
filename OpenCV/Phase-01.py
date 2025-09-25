import cv2

image = cv2.imread("OpenCV\img.png")

if image is not None:
    cv2.imshow("Auto Docs",image) #open the window
    cv2.waitKey(0) #jab tak keyboard se koi key nhi dabai jati tab tak window ko open rkho
    cv2.destroyAllWindows() #close the window
    
else:
    print("Could not load the image")
