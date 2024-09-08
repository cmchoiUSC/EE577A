# Test file for EE577A Lab 1

from prettytable import PrettyTable

input_file = 'LiberateResults.txt'


cellNames = []


class logicCell:
    def __init__(self,name):
        self.name = name
        self.area = 0.00
        self.pin = []

class pin:
        def __init__(self,name,function):
            self.name = name
            self.function = function



#### Parsing Code ####

with open(input_file, 'r') as input:
    content = input.read().split('\n')          # content is a list but content[0] is a str

    for i,val in enumerate(content):
        # print(i,val)
        for j, words in enumerate(val.split()):
            # print(j, words)
            if words == "cell":
                name = val.split()[j+1].replace("(","").replace(")","").replace("{","").replace("}","")
                cellNames.append(logicCell(name))
            if words == "area":
                area = content[i].split()[1].replace(";","")
                cellNames[-1].area = area
            if words == "pin":
                name = val.split()[j+1].replace("(","").replace(")","").replace("{","").replace("}","")
        if "function" in val:
            function = val.replace("function : ", "").replace(";", "").replace("      ", "").replace("\"", "")
            cellNames[-1].pin.append(pin(name,function))




#### Writing Code ####

with open('Results.txt', 'w') as results:
    print("Pin names per function: \n", file=results)                               # Prints initial document line

    for i in range(len(cellNames)):                                                 # Begin print section for each cell
        print("Section " + cellNames[i].name + " pins:", file=results)              # Print name for each cell (first line)
        
        for j in range(len(cellNames[i].pin)):                                      # Looping through each cell
            temp = cellNames[i].pin[j].function.replace("("," ").replace(")"," ").replace("{"," ").replace("}"," ").replace("!"," ").replace("+"," ").replace("*"," ").replace("^"," ").split()
            pins = []                                                               # Creates an array to hold all of the pins
            for p in temp:                                                          # For loop to add the cleaned up pins labels into the pins array
                if pins.count(p) < 1: pins.append(p)                                # Only add the pin if it hasn't already been added before

            print("  Function "  + cellNames[i].pin[j].name + " = " + cellNames[i].pin[j].function + "  ==> uses pins: ", end='', file=results)     # First half of pin print statement
            for p in range(len(pins)):                                              # Printing through the pins array... need to make sure the last pin doesn't print with a comma
                if p == len(pins)-1: print(pins[p], file=results)
                else: print(pins[p] + ", ", end='', file=results)



            #### Code for part II #####
            gFunctions = cellNames
            # print (pins)
            for p in range(len(pins)):                                              # looping through the pins to replace letters is P0, P1, P2,...
                gFunctions[i].pin[j].function = gFunctions[i].pin[j].function.replace(pins[p], "P" + str(p))
                # print(gFunctions[i].pin[j].function.replace(pins[p], "P" + str(p)))
            #### Code for part II #####
                


        print("Total area = " + cellNames[i].area + "\n", file=results)             # Print area for each cell (last line)









    #### Bracket Code ####

    table = PrettyTable()
    table.field_names = ["Expression", "Gates"]


    for i in range(len(gFunctions)):  
        for j in range(len(gFunctions[i].pin)):
            table.add_row([gFunctions[i].pin[j].function, "['" + gFunctions[i].name + "']"])



    print("", file=results)
    print(table, file=results)




