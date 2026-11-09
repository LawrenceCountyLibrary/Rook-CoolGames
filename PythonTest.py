print ("Hello World") #this prints hello world
print ("Hello Universe")   #this prints hello universe
#this code will have varibles and math
hi = 22
hello = 55
hi_and_hello = hi + hello
def spend_hi_hello_points():
    global hi_and_hello
    print("You have "+ str(hi_and_hello) +" Hi And Hello points!") #This gives you the amount of Hi And Hello Points
    print("How many Hi And Hello Points do you want to spend?\n")
    spend = input("Amount: ")
    spend = int(spend)
    newtotal = hi_and_hello-spend
    print("\nYou are spending "+ str(spend) +" Hi And Hello Points!")
    print("That means you will have "+ str(newtotal) +" left.")
    hi_and_hello = newtotal
    return hi_and_hello
spend_hi_hello_points()

print ("|                    |")
print ("|                    |")
print ("|                    |")
print ("                      ")
print ("                      ")
print ("  |                |  ")
print ("   |              |   ")
print ("    ||||||||||||||    ")

spend_hi_hello_points()