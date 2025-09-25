import cv2

img = input("Enter file Location: ")
image = cv2.imread(img)

def draw_line():
    x1 = int(input("Enter coordinate of x1: "))
    y1 = int(input("Enter coordinate of y1: "))
    x2 = int(input("Enter coordinate of x2: "))
    y2 = int(input("Enter coordinate of y2: "))
    color = input("Enter color format e.g.'(255,0,0)': ")
    color_tuple = tuple(map(int,color.strip("()").split(",")))
    thickness = int(input("Enter thickness of line: "))
    cv2.line(image, (x1,y1), (x2,y2), color_tuple, thickness)
    cv2.imshow("Draw_line",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_circle():
    x = int(input("Enter coordinate of x (for center): "))
    y = int(input("Enter coordinate of y (for center): "))
    radius = int(input("Enter radius: "))
    color = input("Enter color format e.g.'(255,0,0)': ")
    color_tuple = tuple(map(int,color.strip("()").split(",")))
    thickness = int(input("Enter thickness of line: "))

    cv2.circle(image, (x,y), radius, color_tuple, thickness)
    cv2.imshow("Draw_circle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_rectangle():
    x1 = int(input("Enter coordinate of x1: "))
    y1 = int(input("Enter coordinate of y1: "))
    x2 = int(input("Enter coordinate of x2: "))
    y2 = int(input("Enter coordinate of y2: "))
    color = input("Enter color format e.g.'(255,0,0)': ")
    color_tuple = tuple(map(int,color.strip("()").split(",")))
    thickness = int(input("Enter thickness of line: "))
    
    cv2.rectangle(image,(x1,y1),(x2,y2),color_tuple, thickness)
    cv2.imshow("Draw_rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

def write_text():
    x = int(input("Enter coordinate of x (for center): "))
    y = int(input("Enter coordinate of y (for center): "))
    text = input("Enter text which you want to put on image: ")
    color = input("Enter color format e.g.'(255,0,0)': ")
    color_tuple = tuple(map(int,color.strip("()").split(",")))
    thickness = int(input("Enter thickness of line: "))

    cv2.putText(image, text,(x,y), cv2.FONT_HERSHEY_PLAIN, 1.2, color_tuple, thickness)
    cv2.imshow("Write_text",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if image is not None:
    print("1 for line draw")
    print("2 for circle draw")
    print("3 for rectangle draw")
    print("4 for custom text")
    choice = input("Enter Your choice: ")

    match choice:
        case '1':
            draw_line()
        case '2':
            draw_circle()
        case '3':
            draw_rectangle()
        case '4':
            write_text()
        case _:
            print("Invalid choice")
else:
    print("Error: file is not load!!")