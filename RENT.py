import Functions

'''---------------------------------------------------------------------------------------------------------------'''
    
def validQuantity(mainData, SN):
    valid_data = False
    while valid_data == False:
        try:
            quantity = int(input("How many pieces do you want to rent? "))
            print()
            if quantity > 0 and quantity <= int(mainData[SN][3]):
                    valid_data = True
                    return quantity
            else:
                 print()
                 print("|==========================================================|")
                 print("|         Sorry!!! Out of our costume's range.             |")
                 print("|==========================================================|\n")

        except:

            print("\n============================")
            print("    Invalid input!!!!!")
            print("=============================\n")
            

'''---------------------------------------------------------------------------------------------------------------'''


def validId(mainData):
    valid_data = False
    while valid_data == False:
        try:
            SN = int(input("Enter the ID of the costume you want to rent: "))   
            print()
            if SN > 0 and SN <= len(mainData):
                if int(mainData[SN][3]) > 0:
                    valid_data = True
                    return SN 
                else:
                    print()
                    print("|===========================================================|")
                    print("|             Sorry the costume is not in stock!!!          |")
                    print("|===========================================================|\n")
            else:
                print("|===========================================================|")
                print("|                    Invalid ID!!                           |")
                print("|===========================================================|\n")

        except:
            print("\n============================")
            print("    Invalid input!!!!!")
            print("=============================\n")
            

'''--------------------------------------------------------------------------------------------------------------'''
    
def rent():
    print("\n Let's rent a costume. \n")
   
    fileContent = Functions.getFileContents()
    mainData = Functions.getDictionary(fileContent)

    cart = []
    continueLoop = True
    while continueLoop == True:
        Functions.printCostumes()
        SN = validId(mainData)
        print()
        print("|==========================================================|")
        print("|               Costume is available for rent!!            |")
        print("|==========================================================|\n")
        quantity = int(validQuantity(mainData, SN))
        mainData[SN][3] = int(mainData[SN][3]) - quantity
        cart.append([SN, quantity])

        Functions.writeFile(mainData)
        Functions.printCostumes()

        while True:
            userInput = input("Do you want to rent more costumes?(yes/no) ")
            
            if userInput.upper() == "NO":
                continueLoop = False
                break

            elif userInput.upper()=="YES":
                break
            
            else:
                print("=====================================================")
                print("                  Invalid input " )
                print("===================================================== \n")
                continueLoop = True
   
    print()
    Bill(cart)
    print()
    print("|===========================================================|")
    print("|           Thank you. The costume has been rented.         | ")
    print("|===========================================================|\n")
    
'''--------------------------------------------------------------------------------------------------------'''

def Bill(cart):
   
    file_content = Functions.getFileContents()
    mainData = Functions.getDictionary(file_content)
    date = Functions.date_time()
    dater = Functions.dateTime()

    nn = False
    while nn == False:
        
            name = input("Please enter your name: ")
            if name.isalpha():
                nn = True

            else:
                print("\n============================")
                print("    Invalid input!!!!!")
                print("=============================\n")
            
    nm = False       
    while nm == False:
        
        try:
            no =int(input("Please enter your contact number: "))
            nm = True
            
        except:
            print("\n============================")
            print("    Invalid input!!!!!")
            print("=============================\n")



        
    file=open("Rent_" + dater +"_" + name + ".txt" ,"w")
    file.write("\n====================================================================")
    file.write("\n                            BILL                                    ")
    file.write("====================================================================\n")
    file.write("\n" + "Name: " + name)
    file.write("\nPhone no.: " + str(no))
    file.write("\nRent Date: " + str(date) + "\n")
       
    file.write("n\-----------------------------------------------------------------------")
    file.write("\nID\tCostume Name\t\tBrand\t\tPrice\tQuantity\n")
    file.write("---------------------------------------------------------------------\n")

    total = 0
    for index in range(len(cart)):
        c_id = int(cart[index][0])
        c_quantity = int(cart[index][1])
        c_name = mainData[c_id][0]
        c_brand = mainData[c_id][1]
        c_price = float(mainData[c_id][2].replace("$", "")) * c_quantity
        total += c_price
        
        file.write(str(index + 1) + "\t" + c_name + "\t" + c_brand + "\t" + str(c_price) + "\t" + str(c_quantity))
        file.write("\n")
       
    file.write("\n Net Total: " + str(total))

    file.close()

    print()
    print("===========================================================================")
    print("                             BILL                                          ")
    print("===========================================================================")
    print("Name: " + name)
    print("Phone no.: " + str(no))
    print("Rent Date: " + str(date))
       
    print("-----------------------------------------------------------------------")
    print("ID\tCostume Name\t\tBrand\t\tPrice\tQuantity")
    print("-----------------------------------------------------------------------\n")

    total = 0
    for index in range(len(cart)):
        c_id = int(cart[index][0])
        c_quantity = int(cart[index][1])
        c_name = mainData[c_id][0]
        c_brand = mainData[c_id][1]
        c_price = float(mainData[c_id][2].replace("$", "")) * c_quantity
        total += c_price
       
        print(str(index + 1) + "\t" + c_name + "\t" + c_brand + "\t" + str(c_price) + "\t" + str(c_quantity))
        print("\n")
       
    print("Grand Total: " + str(total))
    print()
    print("---------------------------------------------------------------------------")


'''-------------------------------------------------------------------------------------------------------------'''   
