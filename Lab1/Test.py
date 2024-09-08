# Test file for EE577A Lab 1

from prettytable import PrettyTable

input_file = 'LiberateResults.txt'


cellNames = []


class LogicCell:
    def __init__(self,name):
        self.name = name
        self.area = 0.00
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
        self._keys = []
        self._dict = {}

    def add(self, key, value):
        if key not in self._dict:
            self._keys.append(key)
            self._dict[key] = []
        self._dict[key].append(value)

    def get(self, key):
        return self._dict.get(key, [])
    
    def getKey(self, index):
        if index < len(self._keys):
            # return self._keys[index], self._dict[self._keys[index]][-1]
            return self._keys[index]
        else:
            raise IndexError("Index out of range")
    
    def getSize(self):
        return len(self._dict.keys())

    def delete(self, key=None, value=None):
        if key is not None and key in self._dict:
            if value is not None and value in self._dict[key]:
                if len(self._dict[key]) == 1:
                    del self._dict[key]
                    self._keys.remove(key)
                else:
                    self._dict[key].remove(value)
            else:
                raise ValueError("Value not found")

    def clear(self):
        self._dict.clear()



#### Parsing Code ####

with open(input_file, 'r') as input:
    content = input.read().split('\n')          # content is a list but content[0] is a str

    for i,val in enumerate(content):
        # print(i,val)
        for j, words in enumerate(val.split()):
            # print(j, words)
            if words == "cell":
                name = val.split()[j+1].replace("(","").replace(")","").replace("{","").replace("}","")
                cellNames.append(LogicCell(name))
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



            #### Code for part II #####
            gFunctions = cellNames
            # print (pins)
            for p in range(len(pins)):                                              # looping through the pins to replace letters is P0, P1, P2,...
                gFunctions[i].pin[j].function = gFunctions[i].pin[j].function.replace(pins[p], "P" + str(p))
                # print(gFunctions[i].pin[j].function.replace(pins[p], "P" + str(p)))
            #### Code for part II #####
                


        print(f"Total area = {cellNames[i].area}\n", file=results)             # Print area for each cell (last line)




    #### Part II ####

    md = MultiDict()                                    # Creating MultiDicitonary
    table = PrettyTable()                               # Creating Table
    table.field_names = ["Expression", "Gates"]         # Creating column labels
    table.align["Expression"] = "l"                     # Aligning left column to left side to match example

    for x in range(len(gFunctions)):                                              # Looping through Cells 
        md.add(frozenset(gFunctions[x].getPinNames()), gFunctions[x].name)        # Putting cell pin names into dictionary with cell name
    for x in range(md.getSize()):                                                 # Looping through the dictionary
        table.add_row([list(md.getKey(x)), md.get(md.getKey(x))])                 # Adding dictionary to table
    """
        Note: pin names have been added into the dictionary as a frozenset so as to ignore the ordering of pins Ex: ([“A*B”, “A^B”] = [“A^B”, “A*B”] = “P1*P2/P1^P2”)
              However, these are then changed back into lists when going into the table for formating reasons. 
    """
    print("", file=results)
    print(table, file=results)

