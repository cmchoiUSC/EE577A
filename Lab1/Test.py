# Test file for EE577A Lab 1

from prettytable import PrettyTable

input_file = 'LiberateResults.txt'


cellNames = []


class LogicCell:
    def __init__(self,name):
        self.name = name
        self.area = 0.00
        self.leak = 0.00
        self.lgate = ""
        self.pin = []

    def getPinNames(self):
        ret = []
        for x in self.pin:
            ret.append(x.function)
        return ret
            

class pin:
        def __init__(self,name,function):
            self.name = name
            self.function = function


class MultiDict:
    def __init__(self):
        self.keys = []
        self.dict = {}

    def add(self, key, tup):
        if key not in self.dict:
            self.keys.append(key)
            self.dict[key] = []
        self.dict[key].append(tup)

    def get(self, key):
        return self.dict.get(key, [])
    
    def getKey(self, index):
        if index < len(self.keys):
            return self.keys[index]
        else:
            raise IndexError("Index out of range")
    
    def getSize(self):
        return len(self.dict.keys())



class LeakDict:
    def __init__(self, expression):
        self.expression = expression
        self.data = ("","",0.00)



#### Parsing Code ####

with open(input_file, 'r') as input:
    content = input.read().split('\n')          # content is a list but content[0] is a str

    for i,val in enumerate(content):
        # print(i,val)
        for j, words in enumerate(val.split()):                                                                     # Looping through everything to isolate information and store it in cell variables.
            # print(j, words)
            if words == "cell":
                name = val.split()[j+1].replace("(","").replace(")","").replace("{","").replace("}","")
                cellNames.append(LogicCell(name))
                currCell = cellNames[-1]
            if words == "area":
                area = content[i].split()[1].replace(";","")
                currCell.area = area
            if words == "pin":
                name = val.split()[j+1].replace("(","").replace(")","").replace("{","").replace("}","")
            if words == "leakage_power":
                value = float(content[i+1].split()[1].replace(";",""))
                if value > currCell.leak:
                    currCell.leak = value
                    currCell.lgate = content[i+2].replace("      when  (", "").replace(");", "")

        if "function" in val:
            function = val.replace("function : ", "").replace(";", "").replace("      ", "").replace("\"", "")
            currCell.pin.append(pin(name,function))




#### Writing Code ####

with open('Results.txt', 'w') as results:
    print("Pin names per function: \n", file=results)                               # Prints initial document line

    for i in range(len(cellNames)):                                                 # Begin print section for each cell
        print(f"Section {cellNames[i].name} pins:", file=results)                   # Print name for each cell (first line)
        
        for j in range(len(cellNames[i].pin)):                                      # Looping through each cell
            temp = cellNames[i].pin[j].function.replace("("," ").replace(")"," ").replace("{"," ").replace("}"," ").replace("!"," ").replace("+"," ").replace("*"," ").replace("^"," ").split()
            pins = []                                                               # Creates an array to hold all of the pins
            for p in temp:                                                          # For loop to add the cleaned up pins labels into the pins array
                if pins.count(p) < 1: pins.append(p)                                # Only add the pin if it hasn't already been added before

            print(f"  Function {cellNames[i].pin[j].name} = {cellNames[i].pin[j].function}  ==> uses pins: ", end='', file=results)     # First half of pin print statement
            for p in range(len(pins)):                                              # Printing through the pins array... need to make sure the last pin doesn't print with a comma
                if p == len(pins)-1: print(pins[p], file=results)
                else: print(pins[p] + ", ", end='', file=results)



            #### Setup Code for part II #####
            gFunctions = cellNames
            for p in range(len(pins)):                                              # looping through the pins to replace letters is P0, P1, P2,...
                gFunctions[i].pin[j].function = gFunctions[i].pin[j].function.replace(pins[p], "P" + str(p))
            ###################################

        print(f"Total area = {cellNames[i].area}\n", file=results)             # Print area for each cell (last line)




    #### Part II ####

    md = MultiDict()                                    # Creating MultiDicitonary
    ml = MultiDict()
    table = PrettyTable()                               # Creating Table
    table.field_names = ["Expression", "Gates"]         # Creating column labels
    table.align["Expression"] = "l"                     # Aligning left column to left side to match example


    for x in gFunctions:
        temp = x.lgate.replace("!"," ").replace("&"," ").split()
        pins = []
        for p in temp:
            if pins.count(p) < 1: pins.append(p)
        
        for p in range(len(pins)):
            x.lgate = x.lgate.replace(pins[p], f"P{p}").replace("&","*")



    for x in range(len(gFunctions)):                                                                                        # Looping through Cells 
        md.add(frozenset(gFunctions[x].getPinNames()), gFunctions[x].name)                                                  # Putting cell pin names into dictionary with cell name
        ml.add(frozenset(gFunctions[x].getPinNames()), (gFunctions[x].name, gFunctions[x].lgate, gFunctions[x].leak))
    for x in range(md.getSize()):                                                                                           # Looping through the dictionary
        table.add_row([list(md.getKey(x)), md.get(md.getKey(x))])                                                           # Adding dictionary to table
    """
        Note: pin names have been added into the dictionary as a frozenset so as to ignore the ordering of pins Ex: ([“A*B”, “A^B”] = [“A^B”, “A*B”] = “P1*P2/P1^P2”)
              However, these are then changed back into lists when going into the table for formating reasons. 
    """
    print("", file=results)
    print(table, file=results)

    print("\n\nMaximum Leakage Scenarios For Each Logic Group\n ", file=results)

    for x in range(ml.getSize()):
        print(f"Expression {list(ml.getKey(x))}", file=results)

        table = PrettyTable()
        table.field_names = ["Gates", "MinTerm", "Leakage Value"]
        table.align["Gates"] = "l"
        

        for y in range(len(ml.get(ml.getKey(x)))):
            temp = ml.get(ml.getKey(x))[y]
            table.add_row([temp[0], temp[1], temp[2]])


        print(f"{table}\n", file=results)