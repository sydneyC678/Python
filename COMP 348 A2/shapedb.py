import os.path
from Shapes import Shape
from Shapes import Circle
from Shapes import Ellipse
from Shapes import Rhombus
#Functions for the assignment
def isShape(row_content):
    if row_content[0] in ["shape", "circle", "ellipse", "rhombus"]:
        return True
    else:
        return False

#shape_count = 0
circle_count = 0
ellipse_count = 0
rhombus_count = 0
count_rows = 0
error_count = 0

filename = "file.txt"

def LOAD(filename):
    global circle_count
    global ellipse_count
    global rhombus_count
    global error_count
    global count_rows
    if os.path.isfile(filename):
        print(f"Processing {os.path.abspath(filename)}")
    #open file for reading
        file_object = open(filename, "r")

    #read the content of each line of the text file
        for line in file_object:
            row_content = line.split()  # Split the line into elements based on space
            count_rows += 1  # Increment row count

            if isShape(row_content):
            #if this is true, then we keep going
            
            #test for each case
                if row_content[0]=="shape":
                #make sure the parameters is set to 0
                    if len(row_content)>1:
                        error_count +=1
                        print(f"Error: Invalid Shape On Line {count_rows}:", line, end = "")
                        continue;
                    else: #keep going
                        shape = Shape()
                        multiset.append(shape)
                if row_content[0] == "circle":
                    if (len(row_content) != 2): #if there is more than one parameter and less than one parameter
                        error_count +=1
                        print(f"Error: Invalid Circle On Line {count_rows}:", line, end = "")
                        continue;
                    elif int(row_content[1])<0: #if the parameter is a negative number
                        error_count +=1
                        print(f"Error: Invalid Circle On Line {count_rows}:", line, end = "")
                        continue;
                    else: #all clear
                        circle = Circle(int(row_content[1]))
                        multiset.append(circle)
                        circle_count += 1
                if row_content[0]=="ellipse":
                #two parameters
                    if len(row_content) !=3:
                        error_count +=1
                        print(f"Error: Invalid Ellipse On Line {count_rows}:", line, end = "")
                        continue;
                    elif int(row_content[1]) < 0 or int(row_content[2])<0: #make sure values are not negative
                        error_count +=1
                        print(f"Error: Invalid Ellipse On Line {count_rows}:", line, end = "")
                        continue;
                    else:
                        ellipse = Ellipse(int(row_content[1]), int(row_content[2]))
                        multiset.append(ellipse)
                        ellipse_count +=1 
                    
                if row_content[0]=="rhombus":
                #two parameters
                    if len(row_content) !=3:
                        error_count +=1
                        print(f"Error: Invalid Rhombus On Line {count_rows}:", line, end = "")
                        continue;
                    elif int(row_content[1]) < 0 or int(row_content[2])<0: #make sure values are not negative
                        error_count +=1
                        print(f"Error: Invalid Ellipse On Line {count_rows}:", line, end = "")
                        continue;
                    else:
                        rhombus = Rhombus(int(row_content[1]), int(row_content[2]))
                        multiset.append(rhombus)
                        rhombus_count+=1
                    

            else:
                print(f"Error: Not A Valid Shape Name On Line {count_rows}:", line, end = "") 

        file_object.close()
        print(f"Processed {count_rows} row(s), {Shape.shape_count} shape(s) added, {error_count} error(s)")
    else:
        print(f"File '{filename}' does not exist.")

def TOSET():
    #convert multi set in memory to a set
    shaped = set(multiset)
    unique_set = set()

    for obj in shaped:
        duplicate = False
        for obj2 in unique_set:
            if obj == obj2:
                duplicate = True
                break
        if not duplicate:
            unique_set.add(obj)

    return list(unique_set)
    

def SAVE(file_name):
    file_object = open(file_name, "w")

    for shape in multiset:
        file_object.write(str(shape) + "\n")

    file_object.close()

def PRINT():
    count = 1
    for shape in multiset:
        print(f"{count}: {shape.print()}")
        count += 1

def SUMMARY():
    global circle_count
    global ellipse_count
    global rhombus_count
    
    print("Circle(s):", circle_count)
    print("Ellipse(s):", ellipse_count)
    print("Rhombus(es):", rhombus_count)
    print("Shape(s):", Shape.shape_count)
    
def DETAILS():
    if len(multiset) == 0:
        print("Error. No shapes to show details for.")
   
    else:
        shapes = []
        shapes = []
        circles = []
        ellipses = []
        rhombuses = []

        for shape in multiset:
            shape_name = shape.__class__.__name__.lower()
            if isinstance(shape, Circle):
                circles.append((shape_name, shape.radius))
            elif isinstance(shape, Ellipse):
                ellipses.append((shape_name, shape.a, shape.b))
            elif isinstance(shape, Rhombus):
                rhombuses.append((shape_name, shape.d1, shape.d2))
            else:
                shapes.append(shape_name)

        for shape in shapes:
            print(*shape)
        for circle in circles:
            print(*circle)
        for ellipse in ellipses:
            print(*ellipse)
        for rhombus in rhombuses:
            print(*rhombus)

def QUIT():
    print("Thank you for using my application! Now quitting the program.")
    exit()

if __name__== "__main__":
    multiset = []
    while True:
        choice = input("Enter choice: LOAD, TOSET, SAVE, PRINT, SUMMARY, DETAILS, QUIT: ")
        if(choice == "LOAD"):
            filename = input("Enter name of file you wish to load: ")
            LOAD(filename)
        elif(choice == "TOSET"):
            multiset = TOSET()
        elif(choice == "SAVE"):
            filename2 = input("Enter name of file name you wish to save: ")
            SAVE(filename2)
        elif(choice == "PRINT"):
            PRINT()
        elif(choice == "SUMMARY"):
            SUMMARY()
        elif(choice == "DETAILS"):
            DETAILS()
        elif(choice == "QUIT"):
            QUIT()
        else:
            continue
            












