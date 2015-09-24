import turtle
print("You are given 'x' amount of fence to enclose a rectangular area.")
print("The amount of fence given is used to fence 3 sides of the area. ")
print("'a' will be the length of the 2 sides, whereas 'b' will be the length of the width or remaining side.\n")
x = int(input("How much fence are you given? \n"))
a = (3/8)*x
b = (1/4)*x
area = (3/32)*(x**2)
print("The optimum value of the length 'a' would be ", a)
print(" ")
print("The optimum value of the width 'b' would be ", b)
print(" ")
print("The optimum area given by these dimensions would be ", area)
choice = int(input("Would you like to see this area drawn out? Enter 1 for yes, or 0 for no.\n"))
if choice == 1:
    turtle.showturtle()
    turtle.color("Blue")
    turtle.penup()
    turtle.setpos((-1/2)*b, (-1/2)*a)
    turtle.pendown()
    turtle.forward(b)
    turtle.left(90)
    turtle.color("Black")
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.mainloop()
    print("Thank you for using this tool!")
else:
    print("Thank you for using this tool!")
    