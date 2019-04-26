def cleanInput(slipknot):#defines a function called clean input taking 1 parameter
    userInput = input(slipknot)# asking and storing a userinput within the the parameters
    print("*****NEWLINE*****")
    return userInput


name = cleanInput("Enter your name")
villagename = cleanInput("Enter a place")
location = cleanInput("enter a different place")
object = cleanInput("Enter an object")

print("There was a butcher called "+ name +" who killed everyone in "+ villagename +"with a "+ object +" he went to "+ location +"")