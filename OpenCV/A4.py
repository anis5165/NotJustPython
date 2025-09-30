import cv2

img = input("Enter your image url: ")
image = cv2.imread(img)

def draw_contours():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray, 200, 255,cv2.THRESH_BINARY) 

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(image, contours, -1, (255,0,0),2)
    cv2.imshow("contours", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def find_shapes():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,200,255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        corner = len(approx)

        if corner == 3:
            shape = 'Triangle'
        elif corner == 4:
            shape = 'Rectangle'
        elif corner == 5:
            shape = 'Pentagon'
        elif corner > 5:
            shape = 'Circle'
        else:
            shape = 'Unknown'

        cv2.drawContours(image, contour, -1, (0,255,0),2)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 10
        cv2.putText(image, shape, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255))
    
    cv2.imshow("Detect Shape using contours", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def main():
    print("1 for Draw contours")
    print("2 for Find shapes")

    choice = input("Enter your choice: ")

    if choice == '1':
        draw_contours()
    elif choice == '2':
        find_shapes()
    else:
        print("Invalid Choice!!")


if __name__ == "__main__":
    main()