# Test file for EE577A Lab 1


input_file = 'LiberateResults.txt'


cell, area = False, False
cellNames = []



# class logicCell:
#     def __init__(self,name,area):
#         self.name = name
#         self.area = area
#         self.function = "function"


# with open(input_file, 'r') as input:
#     content = input.read().split('\n')          # content is a list but content[0] is a str

#     for i,val in enumerate(content):
#         # print(i,val)
#         for j, words in enumerate(val.split()):
#             # print(j, words)
#             if words == "cell":
#                 name = val.split()[j+1].replace("(","").replace(")","").replace("{","").replace("}","")
#                 area = content[i+1].split()[1].replace(";","")
#                 cellNames.append(logicCell(name, area))

# for x in cellNames:
#     print(x.name, x.area)

name = ""
area = 0.00


class logicCell:
    def __init__(self,name):
        self.name = name
        self.area = 0.00
        self.pin = []

class pin:
    def __init__(self, name):
        self.name = name


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
                cellNames[-1].pin.append(name)

            

for x in cellNames:
    print(x.name, x.area, x.pin)