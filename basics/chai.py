# from index import chai

# chai("timer")


# Grade calculator 

grade = int(input("Enter grade : "))

if grade >= 101:
    print("Please verify your grade again")
    exit()

if grade >=90:
    print("A")
elif grade >=80:
    print("B")
elif grade >=70:
    print("C")
elif grade >=60:
    print("D")
else:
    print("F")