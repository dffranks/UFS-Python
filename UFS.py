from os.path import exists
from decimal import Decimal
import time

# Global variables
targetFile = ""
bal = spent = round(Decimal(0.00), 2)
transactList = {1:'Food/Coffee', 2:'Grocery/Supply', 3:'"Stuff"', 4:'Booze', 5:'Gas',
                6:'Car_Payment/Insurance', 7:'Rent', 8:'Utilities/Internet',
                9:'Student_Loan', 10:'Misc_Payment', 11:'Misc_Expense',
                12:'Paycheck', 13:'Deposit'}

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
                if 
                fileID -= 1
                fileName = "PayPeriod_%d.ufs" % fileID
                break

    # Open file for appending
    print "Opening %s!" % fileName
    global targetFile
    targetFile = open(fileName, 'a+')
    # if targetFile.read() == "":
    #     targetFile.write("File Created on %s\n---------------------------\n" % time.strftime("%m-%d-%y"))

# Take in user input
def userInput():

    # Take in user input until 'x' is inputted
    while True:
        print "Input a new transaction amount. When done, input 'x'."
        userIn = raw_input('>> ')
        if userIn is 'x':
            break
        # Convert string input to rounded decimal value
        try:
            transaction = round(Decimal(userIn), 2)
        except ValueError:
            print "Please enter a valid monetary value!"
            continue

        print "Please input Transaction ID from list:"
        for k in transactList:
            print "   %r\t=   %s" % (k, transactList[k]) 

        # Ask for selection until valid input received
        while True:
            userIn = raw_input('>> ')
            # Convert string input to int
            try:
                transactType = int(userIn)
                # If input is 1 - 9
                if 1 <= transactType <= 11:
                    print "Debiting $%s as a(n) %s expenditure." % (transaction, transactList[transactType])
                    transaction *= -1
                    break
                # If input is 10 - 11
                elif 12 <= transactType <= 13:
                    print "Crediting $%s via your %s." % (transaction, transactList[transactType])
                    break
                else:
                    print "Invalid Transaction ID!"
            except ValueError:
                print "Please enter a valid selection!"
                continue

        global bal
        bal += transaction

        fileWrite(transaction, transactList[transactType])
        
    feedback()


def fileWrite(trans, transType):

    line =  "%8s  %8s  %s\n" % (time.strftime("%m-%d-%y"), trans, transType)
    print line
    targetFile.write(line)

def feedback():
    print """
    Your current balance is %s
    You have earned [unfinished].
    You have spent [unfinished].""" % (bal)

# Main function
if __name__ == "__main__":
    print """
========================================
 Welcome to SimpleUFS - Python Edition!
========================================\n"""

    fileOpen(isNewPeriod())
    userInput()
