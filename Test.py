# Test file for EE577A Lab 1

# import re

# input_file = 'LiberateResults.txt'
# output_file = 'Results.txt'


# def extract_cell_names(input_file_path):
#     try:
#         with open(input_file_path, 'r') as input_file:
#                 content = input_file.read()

#                 # Use a regular expression pattern to find "cell (**name**)" occurrences
#                 pattern = r"cell \("
#                 cell_names = re.findall(pattern, content)

#                 # Print the extracted cell names and write them to a new .txt file
#                 print(f"Found {len(cell_names)} cell name(s):")
#                 for index, name in enumerate(cell_names):
#                     print(f"{index+1}. {name}")
                
#                 output_file_path = 'cell_names.txt'  # You can change this path as needed

#                 with open(output_file_path, 'w') as output_file:
#                     for name in cell_names:
#                         output_file.write(name + "\n")

#     except FileNotFoundError:
#             print("Error: File not found")
#     except Exception as e:
#          print(f"An error occured: {str(e)}")

# extract_cell_names(input_file)

# with open(input_file, 'r') as input:
#     content = input.read()
#     content.find("cell")



# with open(output_file, 'w') as output:
#     output.write("hello")




input_file = 'LiberateResults.txt'

cell, area = False, False


cellNames = []

class logicCell:
    def __init__(self,name,area):
        self.name = name
        self.area = area
        self.pins = "pins"
    



# above = []
# one = logicCell()
# two = logicCell()

# above.append(one)
# above.append(two)
# print(above[1].name)
# above[-1].name = "howdy"
# print(above[1].name)



with open(input_file, 'r') as input:
    content = input.read().split('\n')          # content is a list but content[0] is a str

    for i,val in enumerate(content):
        # print(i,val)
        for j, words in enumerate(val.split()):
            # print(j, words)
            if words == "cell":

                name = val.split()[j+1].replace("(","").replace(")","").replace("{","").replace("}","")
                area = content[i+1].split()[1].replace(";","")
                cellNames.append(logicCell(name, area))
                
for x in cellNames:
    print(x.name, x.area)


