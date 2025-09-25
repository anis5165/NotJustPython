import cv2

user_input = input("Enter Your Image file name: ")

image = cv2.imread(user_input)

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    choice = input("Choose one these following - For show (sh) and for save (sa): ")
    if choice == 'sh':
        cv2.imshow("Kaam-wali",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 'sa':
        fileName = input("Enter File Name: ")
        success = cv2.imwrite(fileName, gray)
        if success:
            print(f"File successfully saved '{fileName}'") 
        else:
            print("Failed to save file")
else:
    print("Error: Failed to load file")
