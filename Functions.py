
'''-----------------------------------------------------------------------------------------------------------'''

def getFileContents():
    file = open("costumes.txt", "r")
    data = file.readlines()
    file.close()
    return data

'''-------------------------------------------------------------------------------------------------------------'''

def getDictionary(fileContent):
    data = {}
    for index in range(len(fileContent)):
        data[index + 1] = fileContent[index].replace("\n", "").split(",")
    return data

'''--------------------------------------------------------------------------------------------------------------'''

def printCostumes():
    fileContent = getFileContents()
    mainData = getDictionary(fileContent)
    print("-------------------------------------------------------------------------")
    print("ID", "\t", "Costume Name", "\t\t", "Brand", "\t\t", "Price", "\t", "Quantity ")
    print("------------------------------------------------------------------------\n")
    for key,value in mainData.items():  
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t", value[3])

    print("\n-------------------------------------------------------------------------\n")

'''--------------------------------------------------------------------------------------------------------------'''            
    

def writeFile(mainData): 
    file = open("costumes.txt", "w")
    for value in mainData.values():
        write_data = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n"
        file.write(write_data)
    file.close()

'''----------------------------------------------------------------------------------------------------------------'''

def date_time():
    import datetime
    date1= (datetime.datetime.now().year)
    date2= (datetime.datetime.now().month)
    date3= (datetime.datetime.now().day)
    date4= (datetime.datetime.now().hour)
    date5= (datetime.datetime.now().minute)
    date6= (datetime.datetime.now().second)
    date7=(str(date1)+("/")+str(date2)+("/")+str(date3)+("/")+str(date4)+(":")+str(date5)+(":")+str(date6))
    
    return date7


'''---------------------------------------------------------------------------------------------------------------'''

def dateTime():
    import datetime
    date1= (datetime.datetime.now().year)
    date2= (datetime.datetime.now().month)
    date3= (datetime.datetime.now().day)
    date4= (datetime.datetime.now().hour)
    date5= (datetime.datetime.now().minute)
    date6= (datetime.datetime.now().second)
    date7=(str(date1)+("_")+str(date2)+("_")+str(date3)+("_")+str(date4)+("_")+str(date5)+("_")+str(date6))
    
    return date7


'''---------------------------------------------------------------------------------------------------------------'''


