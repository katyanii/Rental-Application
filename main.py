import RENT
import RETURN
import Exit
'''---------------------------------------------------------------------------------------------------------------'''
print()
print("========================================================================")
print("          Welcome to Costume Rental Application                         ")
print("======================================================================\n")
print()


'''---------------------------------------------------------------------------------------------------------------'''


loop = True

while loop == True:       
    print("Select a desirable option")
    print("a: Press 1 to rent a costume.")
    print("b: Press 2 to return a costume.")
    print("c: Press 3 to exit.\n")

    il = True
    while il == True:
    
          try:

            K = int(input("Select an option: "))
            il = False

          except:
            print("\n======================================================")
            print("                  Invalid input!!!!!")
            print("======================================================\n")
            
    
    if K == 1:
        RENT.rent()


    elif K == 2:
        RETURN.Return()
        

    elif K == 3:
        Exit.exit()
        loop = False

    else:
        print("\n======================================================")
        print("                  Invalid input!!!!!")
        print("======================================================\n")
