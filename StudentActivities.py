# This is a rough draft of a program I designed for student activities.
# It's not complete and I'm still working on it.
# However I'm hoping to...use it to help with answering repetitive questions.

Name = input("What is your name? ")  # First I ask the Students name
# Then I welcome them to the department
print("Hello, " + Name + "! Welcome to student Activities!")
# I then prompt the student to ask for help.
user_input = input(
    "What can we help you with today? Type ID, Parking Pass, or Both:  ")

# This is the student ID function.


def Student_ID(user_input):  # The argument is the user input
    if user_input == "ID":
        print("Okay " + Name + "Are you a new or returning student?")
        # Ask the Student if they are new or returning
        new_returning = input(" type 'new' or 'returning' : ")
        if new_returning == "new":
            # Ask the student if they are registered for the current semester
            print("Do you have proof of your registration for the current semester?")
            registration = input(" Type 'yes' or 'no': ")
            if registration == "yes":
                # if they are registered they can go to the front desk and show the receipt to receive and ID
                print("Great! You are all set! " + Name +
                      ", please present your reciept to the receptionist at the front desk.")
        elif new_returning == "returning":
            # If they are not registered they can purchase a replacement ID
            print(
                "Please visit the Cashier in the Dogwood Building to purchase a replacement ID ($5.00)")
            # If they have proof of the replacement ID receipt they can go to the front desk and show the receipt to receive and ID
            replacement_receipt = input("Do you have a replacement receipt? ")
            if replacement_receipt == "yes":
                # If the students registration is valid they can go to the front desk and show the receipt to receive and ID
                print("Do you have proof of your registration for the current semester?")
                registration = input("Yes or No?: ")
                if registration == "yes":
                    print("Great! You are all set! " + Name +
                          ", please present your reciept to the receptionist at the front desk.")
                elif registration == "no":
                    # Display a message to direct the student to the Financial Aid Office.
                    print("Sorry " + Name + ", you are not registered for the current semester. Please visit the financial aid office in the WLC building to print off proof of registration.")
            elif replacement_receipt == "no":
                # re-direct the student to the Cashier's Office to purchase a replacement ID ($5.00)
                print("I'm sorry " + Name + "You will need a receipt to get a replacement ID. Please visit the Cashier in the Dogwood Building to purchase a replacement ID ($5.00)")


# This is the  parking pass function

def Parking_Pass(user_input):
    if user_input == "Parking Pass":
        print("Okay " + Name + ", Are you a new or returning student?")
        user_input = input("New or Returning?: ")
        if user_input == "new":
            print("Awesome!" + Name +
                  "Do you have your receipt showing you've registered for the current semester? ")
            registration = input("Yes or No?: ")
            if registration == "yes":
                print("Great! You are all set! " + Name +
                      ", please present your reciept to the receptionist at the front desk.")
                print("Please note that if you do not know your liscence plate number you can fill out the form and return it to the receptionist at a later time.")
            elif registration == "no":
                print("Sorry " + Name + ", you are not registered for the current semester. Please visit the financial aid office in the WLC building to print off proof of registration.")
        elif user_input == "returning":
            print("Welcome Back! " + Name +
                  ", Do you need another parking pass? ")
            new_pass = input("Yes or No?: ")
            if new_pass == "yes":
                print(
                    "Please visit the Cashier in the Dogwood Building to purchase an additional parking pass ($2.00)")
            elif new_pass == "no":
                print("I'm sorry " + Name +
                      "I'm afraid I don't know what you are looking for.")


# This is the both function


def Both(user_input):
    if user_input == "Both":
        print("Okay " + Name + ", Are you a new or returning student?")
        user_input = input("New or Returning?: ")
        if user_input == "new":
            print("Awesome!" + Name +
                  "Do you have your receipt showing you've registered for the current semester? ")
            registration = input("Yes or No?: ")
            if registration == "yes":
                print("Great! You are all set! " + Name +
                      ", please present your reciept to the receptionist at the front desk.")
                print("Please note that if you do not know your liscence plate number you can fill out the form and return it to the receptionist at a later time.")
                print(
                    "However you may still take your picture for your student ID. Don't Forget to ask for a student planner!")
            elif registration == "no":
                print("Sorry " + Name + ", you are not registered for the current semester. Please visit the financial aid office in the WLC building to print off proof of registration.")
        elif user_input == "returning":
            print("Welcome Back! " + Name +
                  ", Do you need another parking pass? ")
            new_pass = input("Yes or No?: ")
            if new_pass == "yes":
                print(
                    "Please visit the Cashier in the Dogwood Building to purchase an additional parking pass ($2.00)")
            elif new_pass == "no":
                print("I'm sorry " + Name +
                      "I'm afraid I don't know what you are looking for.")


# This is the main function


def main():
    if user_input == "ID":
        Student_ID(user_input)
    elif user_input == "Parking Pass":
        Parking_Pass(user_input)
    elif user_input == "Both":
        Both(user_input)
    else:
        print("I'm sorry " + Name +
              "I'm afraid I don't know what you are looking for.")


main()


# This is the end of the program.
# I hope you enjoyed it!
