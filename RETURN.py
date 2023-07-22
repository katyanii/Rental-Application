import Functions

'''---------------------------------------------------------------------------------------------------------------'''
def validIdr(mainData):
    valid_data = False
    while valid_data == False:
        try:
            SN = int(input("Enter the ID of the costume you want to return: "))
            print()
            if SN > 0 and SN <= len(mainData):
                valid_data = True
                return SN
            else:
                 print("|===========================================================|")
                 print("|                    Invalid ID!!                           |")
                 print("|===========================================================|")
        except:
            print("\n============================")
            print("    Invalid input!!!!!")
            print("=============================\n")
            
'''------------------------------------------------------------------------------------------------------------'''

def validQuantityr(mainData, SN):
    valid_data = False
    while valid_data == False:
        try:
            quantity = int(input("How many pieces do you want to return? "))
            if quantity > 0:
                valid_data = True
                return quantity

            else:
                print("\n==========================================")
                print("            Invalid Amount                ")
                print("==========================================\n")
 
        except:
            print("\n|===========================================================|")
            print("|                    Invalid input!!                        |")
            print("|===========================================================|\n")

'''------------------------------------------------------------------------------------------------------------'''

def Return():
    
    print("\n Let's return the costumes. \n")
   
    fileContent = Functions.getFileContents()
    mainData = Functions.getDictionary(fileContent)

    cart = []
    continueLoop = True
    while continueLoop == True:
        Functions.printCostumes()
        SN = validIdr(mainData)
    
        quantity = int(validQuantityr(mainData, SN))
        mainData[SN][3] = int(mainData[SN][3]) + quantity
        cart.append([SN, quantity])
        
        Functions.writeFile(mainData)
        Functions.printCostumes()

        while True:
            userInput = input("Do you want to retrun  more costumes?(yes/no)")

            if userInput.upper() == "NO":
                continueLoop = False
                break
                
            elif userInput.upper()=="YES":
                break

            else:
                print("=====================================================")
                print(" Invalid input " )
                print("===================================================== \n")
                continueLoop = True
                  
    print()
    Billr(cart)
    print()
    print("|===========================================================|")
    print("|           Thank you. The costume has been returned!       | ")
    print("|===========================================================|\n")
    
'''---------------------------------------------------------------------------------------------------------------'''
def Billr(cart):
   
    file_content = Functions.getFileContents()
    mainData = Functions.getDictionary(file_content)
    date = Functions.date_time()
    dateS = Functions.dateTime()
    
    nn= False
    while nn==False:
        name = input("Please enter your name: ")
        if name.isalpha():
            nn=True
        else:
            print("\n============================")
            print("    Invalid input!!!!!")
            print("=============================\n")


    nm= False
    while nm==False:
         no =input("Please enter your contact number:")
         if no.isalpha():
            nm= False
            print("\n============================")
            print("    Invalid input!!!!!")
            print("=============================\n")
         else:
            nm=True
                

    ne = False
    while ne ==False:
        try:
            extradays = int(input("How many days has it been since you rented the costume?: "))
            ne = True
        except:
            print("\n============================")
            print("    Invalid input!!!!!")
            print("=============================\n")
            
    print()
    file = open("Return_"+dateS  + "_" + name + ".txt", "w")
    file.write("\n===========================================================================")
    file.write("\n                             BILL                                          ")
    file.write("\n==========================================================================\n")
    file.write("\n" + "Name: " + name)
    file.write("\nPhone no.: " + no)
    file.write("\nRent Date: " + str(date))
    file.write("\nNo of days: " + str(extradays) + "\n")
       
    file.write("-----------------------------------------------------------------------")
    file.write("\nID\tCostume Name\t\tBrand\t\tPrice\tQuantity\n")
    file.write("-----------------------------------------------------------------------\n")

    tfine = 0
    fine = 0
    for index in range(len(cart)):
        c_id = int(cart[index][0])
        c_quantity = int(cart[index][1])
        c_name = mainData[c_id][0]
        c_brand = mainData[c_id][1]
        c_price = float(mainData[c_id][2].replace("$", "")) * c_quantity
        eDays = extradays -5
        
        if eDays > 0:
            fine= eDays * 5 * c_quantity
            tfine += fine
       
        file.write(str(index + 1) + "\t" + c_name + "\t" + c_brand + "\t" + str(c_price) + "\t" + str(c_quantity))
        file.write("\n")
       
    file.write("\nFine: " + str(tfine))
    file.close()

    print()
    print("\n===========================================================================")
    print("                             BILL                                          ")
    print("==========================================================================\n ")
    print("\n" + "Name: " + name)
    print("Phone no.: " + no)
    print("Rent Date: " + str(date))
    print("No of days: " + str(extradays) + "\n")
       
    print("-----------------------------------------------------------------------")
    print("ID\tCostume Name\t\tBrand\t\tPrice\tQuantity")
    print("-----------------------------------------------------------------------\n")

    tfine = 0
    fine = 0
    for index in range(len(cart)):
        c_id = int(cart[index][0])
        c_quantity = int(cart[index][1])
        c_name = mainData[c_id][0]
        c_brand = mainData[c_id][1]
        c_price = float(mainData[c_id][2].replace("$", "")) * c_quantity
        eDays = extradays -5
        
        if eDays > 0:
            fine= eDays * 5 * c_quantity
            tfine += fine
       
        print(str(index + 1) + "\t" + c_name + "\t" + c_brand + "\t" + str(c_price) + "\t" + str(c_quantity))
        print("\n")
       
    print("Fine: " + str(tfine))
    print("============================================================================")
'''--------------------------------------------------------------------------------------------------------------'''


