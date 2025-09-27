import cv2

body_cascade = cv2.CascadeClassifier("_project/haarcascade_fullbody.xml")

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break
    
    # Haar cascades work on grayscale images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    body = body_cascade.detectMultiScale(gray, 1.05, 5) #scalefactor = 1.1 (Reduce image size at each step)


    for (x,y,w,h) in body:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0),2)


    cv2.imshow("Full Body detection", frame)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

camera.release()
cv2.destroyAllWindows() 