# Test file for EE577A Lab 1

from prettytable import PrettyTable

input_file = 'LiberateResults.txt'


cellNames = []


class logicCell:
    def __init__(self,name):
        self.name = name
        self.area = 0.00
        self.pin = {}



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
            cellNames[-1].pin.update({name:function})




#### Writing Code ####

with open('Results.txt', 'w') as results:
    print("Pin names per function: \n", file=results)
                
    for cells in cellNames:
        print("Section " + cells.name + " pins:", file=results)
        for x in range(len(cells.pin)):
            temp = list(cells.pin.values())[x].replace("("," ").replace(")"," ").replace("{"," ").replace("}"," ").replace("!"," ").replace("+"," ").replace("*"," ").replace("^"," ").split()
            pins = []
            for p in temp:
                if pins.count(p) < 1:
                    pins.append(p)

            print("  Function " + list(cells.pin.keys())[x] + " = " + list(cells.pin.values())[x] + "  ==> uses pins: ", end='', file=results)
            for p in range(len(pins)):
                if (p == len(pins)-1):
                    print(pins[p], file=results)
                else:
                    print(pins[p] + ", ", end='', file=results)
        print("Total area = " + cells.area + "\n", file=results)










    #### Bracket Code ####

    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide", 1295, 1158259, 600.5])
    table.add_row(["Brisbane", 5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556, 619.5])
    table.add_row(["Sydney", 2058, 4336374, 1214.8])
    table.add_row(["Melbourne", 1566, 3806092, 646.9])
    table.add_row(["Perth", 5386, 1554769, 869.4])
    print("", file=results)
    print(table, file=results)