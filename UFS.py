from os.path import exists

# bal = 0

# Yes or no input
def userAffirm():
    while True:
        usein = raw_input("Y/N: ").lower()
        if usein == 'y':
            return True
            break
        elif usein == 'n':
            return False
            break
        else:
            print "Please input 'y' or 'n'!"

# Is this a new period (file)?
def isNewPeriod():
    print "Is this a new period?"
    if userAffirm():
        return True
    else:
        return False

# Open (or create) file
def fileOpen(isNew):
    # Initialize fileID to 0
    fileID = 0

    while True:
        # Increment ID and build filename
        fileID += 1
        fileName = "PayPeriod_%d.ufs" % fileID

        # Check if file with fileName does NOT already exist
        if not exists(fileName):
            # Is this a new period? If so, proceed to create new file with current ID
            if isNew:
                break
            # If NOT a new period, subtract 1 from fileID to use most recent file
            else:
                fileID -= 1
                fileName = "PayPeriod_%d.ufs" % fileID
                break

    # Open file for appending
    print "Opening %s!" % fileName
    target = open(fileName, 'a')

# Take in user input
def userInput():
    #transactList = []

    # Take in user input until 'x' is inputted
    while True:
        print "Input a new transaction amount. When done, input 'x'."
        userIn = raw_input('>> ')
        if userIn is 'x':
            break
        # Convert string input to float value
        try:
            transaction = float(userIn)
        except ValueError:
            print "Please enter a valid monetary value!"
            continue

        print """Please input Transaction ID from list:
        1: Food / Coffee (-)
        2: Grocery (-)
        3: "Stuff" (-)
        4: Booze (-)
        5: Gas (-)
        6: Car Payment / Insurance (-)
        7: Student Loan (-)
        8: Misc. Payment (-)
        9: Misc. Expense (-)
        10: Paycheck (+)
        11: Deposit (+)"""

        # Ask for selection until valid input received
        while True:
            userIn = raw_input('>> ')
            # Convert string input to int
            try:
                transactType = int(userIn)
                # If input is 1 - 9
                if 1 <= transactType <= 9:
                    transactMsg = "Debiting %f as an expenditure of ID %i." % (transaction, transactType)
                    break
                # If input is 10 - 11
                elif 10 <= transactType <= 11:
                    transactMsg = "Crediting %f as a deposit of ID %i." % (transaction, transactType)
                    break
                else:
                    print "Invalid Transaction ID!"
            except ValueError:
                print "Please enter a valid selection!"
                continue

        print transactMsg + "\n"

if __name__ == "__main__":
    fileOpen(isNewPeriod())
    userInput()
