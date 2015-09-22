from os.path import exists

bal = 0

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

def isNewPeriod():
    print "Is this a new period?"
    if userAffirm():
        return True
    else:
        return False

def fileOpen(isNew):
    fileID = 0
    while True:
        fileID += 1
        fileName = "PayPeriod_%d.ufs" % fileID
        if not exists(fileName):
            if isNew:
                break
            else:
                fileID -= 1
                fileName = "PayPeriod_%d.ufs" % fileID
                break

    print "Opening %s!" % fileName
    target = open(fileName, 'a')

def userInput():
    transactList = []
    while True:
        print "Input a new transaction amount. When done, input 'x'."
        userIn = raw_input('>> ')
        if userIn is 'x':
            break
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

        while True:
            userIn = raw_input('>> ')
            try:
                transactType = int(userIn)
                if 1 <= transactType <= 9 :
                    transactMsg = "Debiting %f as an expenditure of ID %i." % (transaction, transactType)
                    break
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
