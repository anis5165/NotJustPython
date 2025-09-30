import cv2

camera = cv2.VideoCapture(0)

def check_video_recording():
    while True:
        ret, frame = camera.read()

        if not ret:
            break
        cv2.imshow("video shown",frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
        

def video_recording_and_save():
    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    codec = cv2.VideoWriter_fourcc(*'XVID')
    
    recoded = cv2.VideoWriter("a3video.avi",codec,20,(frame_width, frame_height))
    
    while True:
        ret, frame = camera.read()

        if not ret:
            break
        
        recoded.write(frame)
        cv2.imshow("after recoding", frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    
    camera.release()
    recoded.release()
    cv2.destroyAllWindows()

def face_detection():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

    while True:
        ret, frame = camera.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray,1.1, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,225),2)

            roi_gray = gray[y:y+h, x:x+h]
            roi_color = frame[y:y+h, x:x+h]

            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
            if len(eyes) > 0:
                cv2.putText(frame, "Eyes Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,0,0),2)
            
            smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
            if len(smile):
                cv2.putText(frame, "Smile Detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0),2)

        cv2.imshow("Smart Face Detection",frame)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()


def full_body_detection():
    body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

    while True:
        ret, frame = camera.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = body_cascade.detectMultiScale(gray,1.1,5) #scalefactor = 1.1 (Reduce image size at each step)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

        cv2.imshow("fill body detection", frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

def main():
    print("*" * 40)
    print("1 for check_video recording")
    print("2 for check_video recording and save")
    print("3 for Face detection")
    print("4 for full body detection")

    choice = input("Enter your choice: ")
    match choice:
        case '1':
            check_video_recording()
        case '2':
            video_recording_and_save()
        case '3':
            face_detection()
        case '4':
            full_body_detection()
        case _:
            print("invalid input")

if __name__ == "__main__": 
    main()