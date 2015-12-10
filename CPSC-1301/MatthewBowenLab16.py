#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab16
#Date: 28 September 2015
#Description: Prints all numbers in range.
print("Numbers from 1 to 100")
for i in range(1,101):
    print(i, end=" ")
    i = i+1
print("\n")
print("Numbers from 100 to 1")
for i in range(100,0,-1):
    print(i, end=" ")
    i = i-1
print("\n")
print("Even numbers from 1 to 100")
for i in range(2,101,2):
    print(i,end=" ")
print("\n")
print("Odd numbers from 1 to 100")
for i in range(1,101,2):
    print(i, end=" ")
print(" ")
num = int(input("\nPlease enter an integer: "))
while num <= 0:
    num = int(input("Only positive numbers accepted. Please try again: "))
print("\nNumbers from 1 to %d" %num)
for i in range(1,(num+1)):
    print(i, end=" ")
    i = i+1
print("\n")
print("Numbers from %d to 1" %num)
for i in range(num,0,-1):
    print(i, end=" ")
    i = i-1
print("\n")
print("Even numbers from 1 to %d" %num)
for i in range(2,(num+1),2):
    print(i,end=" ")
print("\n")
print("Odd numbers from 1 to %d" %num)
for i in range(1,(num+1),2):
    print(i, end=" ")