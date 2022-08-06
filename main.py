class square:
    def perimeter(x, y):
        ans = (x * y) * 2
        return float(ans)
    def area(x, y):
        ans = x * y
        return float(ans)

class rectangle:
    def perimeter(x, y):
        ans = (x * y) * 2
        return float(ans)
    def area(x, y):
        ans = x * y
        return float(ans)

class circle:
    def diameter(r):
        ans = 2 * r
        return float(ans)
    def circumference(r):
        ans = 2 * 3.14 * r
        return float(ans)
    def area(r):
        ans = 3.14 * (r * r)
        return float(ans)

global fname 
fname= input("First name: ")
global lname 
lname = input("Last name: ")

def selection():
    selector = input(" •Press (1) to get calculations for circle. \n •Press (2) to get calculations for square. \n •Press (3) to get calculations for rectangle. \n\n < Back (5) \n Select: ")
    if selector == "":
        print("Enter valid input !")
        selection()
    else:
        return selector

def choose_shape(g):
    if g == "1":
        r = float(input("Enter radius of your circle: "))
        selector2 = input(" •Press (A) to calculate Diameter of a circle. \n •Press (B) to calculate Circumference of a circle. \n •Press (C) to calculate Area of a circle. \n\n < Back (5) \n Select: ")
        if selector2 == "A" or selector2 == "a":
            answ = float(circle.diameter(r))
            print("\n Hey "+fname+" "+lname+" Your circule Diameter is: ", answ," \n")
            selection()
        elif selector2 == "B" or selector2 =="b":
            answ = float(circle.circumference(r))
            print("\n Hey "+fname+" "+lname+" Your circule Circumference is: ", answ," \n")
            selection()
        elif selector2 == "C" or selector2 == "c":
            answ = float(circle.area(r))
            print("\n Hey "+fname+" "+lname+" Your circule Area is: ", answ," \n")
            selection()
        elif selector2 == "5":
            selection()

    if  g == "2":
        l1 = float(input("Enter lenght-1 of your square: "))
        l2 = float(input("Enter lenght-2 of your square: "))
        if(l1 != l2):
            print("This is not a square!")
            choose_shape(2)
        selector2 = input(" •Press (A) to calculate Perimeter of a square. \n •Press (B) to calculate Area of a square. \n\n < Back (5) \n Select: ")
        if selector2 == "A" or selector2 == "a":
            answ = float(square.perimeter(l1, l2))
            print("\n Hey "+fname+" "+lname+" Your square Perimeter is: ", answ," \n")
            selection()
        elif selector2 == "B" or selector2 =="b":
            answ = float(square.area(l1, l2))
            print("\n Hey "+fname+" " +lname+" Your circule Area is: ", answ," \n")
            selection()
        elif selector2 == "5":
            selection()

    if  g == "3":
        l1 = float(input("Enter lenght-1 of your rectangle: "))
        l2 = float(input("Enter lenght-2 of your rectangle: "))
        selector2 = input(" •Press (A) to calculate Perimeter of a rectangle. \n •Press (B) to calculate Area of a rectangle. \n\n < Back (5) \n Select: ")
        if selector2 == "A" or selector2 == "a":
            answ =  float(rectangle.perimeter(l1, l2))
            print("\n Hey "+fname+" "+lname+" Your rectangle Perimeter is: ", answ," \n")
            selection()
        elif selector2 == "B" or selector2 =="b":
            answ = float(rectangle.area(l1, l2))
            print("\n Hey "+fname+" "+lname+" Your rectangle Area is: ", answ," \n")
            selection()
        elif selector2 == "5":
            selection()


while True:
    selections = selection()
    if selections != "0":
        g = selections
        choose_shape(g)
    if selections == "0":
        break