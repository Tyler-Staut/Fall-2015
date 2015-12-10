#---------TESTING AREA------------------------------



#---------CODE--------------------------------------

def countdown (max):
    sum = 0
    for i in range(1, max + 1):
        sum += i
    sum = sum / (max)
    return sum
print((countdown(5)))
