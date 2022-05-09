#method definitions
def menu():
    print("welcome to programsings things")
    print("")
    print("1. tell reedol")
    print("")
    print("2. i tell me yoke")
    print("")
    print("3. begone")
    print("")
    print("now do numbering")
    print("") 
    choice = int(input())  
    return choice
#main program


print("")
menuChoice = 0
while menuChoice != 3:
    print("")
    menuChoice = menu()
    
    if menuChoice == 1:
        print("i not know any reedol D:")
    
    elif menuChoice == 2:
        print("oke, why chicken croz roed?")
        print("i am doing no suring in the honestness")