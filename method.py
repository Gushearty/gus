#methods are blocks of code that are executre with a bocmand
#metyhos canb e called anything execpe tkeyaword
#predifned python methods
#methods are created at the top of program in Python
#use ht keyword "def" before the method

#method definition
# this method doesnt have parameters
def cat():
    #code that gets executed when method is called
    print("cat.")
    print("not dog")
    print("is cat")
    print("cat not dog")
    print("dog not cat")
#beginning of program
    
def bar(x, y):
    sum = x + y
    return sum
catt = bar(7,3)

print(catt)