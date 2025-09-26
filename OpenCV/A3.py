import cv2

camera = cv2.VideoCapture(0)

def check_video_recording():
    pass

def video_recording_and_save():
    pass




print("1 for check_video recording")
print("2 for check_video recording and save")

choice = input("Enter your choice: ")
match choice:
    case '1':
        check_video_recording()
    case '2':
        video_recording_and_save()
    case _:
        print("invalid input")



