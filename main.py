phoneNumbers = {'Amal'    : '1111111111',
                "Mohammed": "2222222222",
                "Khadijah": "3333333333",
                "Abdullah": "4444444444",
                "Rawan"   : "5555555555",
                "Faisal"  : "6666666666",
                "Layla"   : "7777777777",
                }
repeat = True
while 1 > 0:
    userInput = input("\n"
                      "To search by name enter (name)\n"
                      "To search by number enter (number)\n"
                      "To add new number enter (new)\n"
                      "Input: ")

    if userInput == 'name':  # اذا كان المدخل "name"
        inputName = input("Enter name: ")
        if phoneNumbers.__contains__(inputName):  # التأكد اذا كان الاسم موجود
            print(inputName + "'s number is", phoneNumbers[inputName])
        else:
            print(inputName, "does not exist")
    ####################################################################
    elif userInput == 'number':  # اذا كان المدخل "number"
        inputNumber = input("Enter number: ")
        if len(inputNumber) != 10:  # التأكد اذا الرقم مكون من 10 ارقام
            print("This is invalid number")
        else:
            found = False
            owner = None
            for key in phoneNumbers:
                if phoneNumbers[key] == inputNumber:  # اذا وجد الشخص يخزن اسمه في متغير "owner"
                    found = True
                    owner = key
            if found:  # التأكد اذا وجد الرقم ام لا عن طريق متغير "found"
                print(phoneNumbers[owner], "belongs to", owner)
            else:
                print("Sorry, the number is not found")
    ####################################################################
    elif userInput == 'new':  # اذا كان المدخل "new"
        newName = input("Enter name: ")
        newNumber = input("Enter number: ")
        if len(newNumber) != 10:  # التأكد اذا كان الرقم مكون من 10 ارقام
            print("number must be 10 numbers long")
        else:
            phoneNumbers[newName] = newNumber
            print(newName, phoneNumbers[newName], "added to dictionary")
    else:
        print("Incorrect input")
# print(phoneNumbers[])
