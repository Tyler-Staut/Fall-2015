cont = "yes"
def add(a,b): #Defines adding function
    print("Adding %d and %d" %(a, b))
    global answer
    answer = a+b
    return answer

def subtract(a,b): #Defines subtracting function
    print("Subtracting %d and %d" %(a,b))
    global answer
    answer = a-b
    return answer

def multiply(a,b): #Defines multiplying function
    print("Multiplying %d and %d" %(a,b))
    global answer
    answer = a*b
    return answer

def divide(a,b): #Defines dividing function
    print("Dividing %d by %d" %(a,b))
    global answer
    answer = a/b
    return answer
def main(): #Defines main function
    global a #Makes 'a' global
    a = int(input("Please enter a number for 'a': ")) #Takes input 'a'
    while a < 0:
        a = int(input("Please enter a number for 'a' that is greater than zero: "))
    global b #Makes 'b' global
    b = int(input("Please enter a number for 'b': ")) #Takes input 'b'
    while b < 0:
        b = int(input("Please enter a number for 'a' that is greater than zero: "))
    menu()
    print(answer)
def menu(): #Defines menu function
    print("Welcome! Please choose from the list below.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    x = int(input("Which would you like to do? "))
    if 1 <= x <= 4: #defines which function gets used
        if x==1:
            return(add(a, b))
        if x==2:
            return(subtract(a, b))
        if x==3:
            return(multiply(a, b))
        if x==4:
            return(divide(a, b))
while cont != "exit": #Makes it so loop will continue unless 'exit' is input
    main()
    cont = input("Type 'exit' to quit, or type anything else to use again. ")
print("Thank you for using!")