# Test file for EE577A Lab 1


input_file = 'LiberateResults.txt'


cellNames = []


class logicCell:
    def __init__(self,name):
        self.name = name
        self.area = 0.00
        self.pin = {}


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
            if words == "function":
                function = val.split()[j+2].replace("\"","").replace(";","")
                cellNames[-1].pin.update({name:function})


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
