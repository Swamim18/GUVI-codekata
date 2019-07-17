ph={}
print("Hello! Welcome to your phonebook.")
Flag=True
while(Flag):
    choice=input("What do you want to do?\nAdd - A\nDelete - D\nSearch - S\nDisplay - I\nUpdate - U\nExit - E\n")
    if(choice=="E"):
        Flag=False
    elif(choice=="A"):
        ph[input("What is the name?\n")]=input("What is the phone number?\n")
        print("New contact added.\n")
    elif(choice=="D"):
        del ph[input("Enter the name of the contact you want to delete.\n")]
        print("Contact deleted.\n")
    elif(choice=="S"):
        print(ph[input("Please enter the name whose contact you want to view.\n")])
    elif(choice=="I"):
        print('\n'.join("{}: {}".format(k, v) for k, v in ph.items()))
    elif(choice=="U"):
        ph.update({input("Enter the name.\n"):input("Enter the number.\n")})
    else:
        print("Invalid Input. Please try again.")
