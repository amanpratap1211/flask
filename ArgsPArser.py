import xml.etree.ElementTree as ET
myTree = ET.parse('x1.xml')
myRoot = myTree.getroot()
print(myRoot)
print(myRoot.tag)
print(myRoot.attrib)
print(myRoot[0].tag)
for x in myRoot[0]:
    print(x.tag)
    print(x.attrib)
for x in myRoot[0]:
    print(x.text)

for x in myRoot.findall("food"):
    print(x.find('item').text, end=": ")
    print(x.find('description').text)

for x in myRoot.iter('price'):
    x.text = str(float(x.text)+10)
    x.set('newprices','yes')

ET.SubElement(myRoot[0], 'new')
for x in myRoot.iter("new"):
    x.text = str("added")

# poping the element
# print(myRoot[2][0].attrib.pop('name'))
# Delete
# print(myRoot.remove(myRoot[2]))

myTree.write("x1.xml")

# XMLexample_stored_in_a_string ='''<?xml version ="1.0"?>
# <States>
#     <state name ="TELANGANA">
#         <rank>1</rank>
#         <neighbor name ="ANDHRA" language ="Telugu"/>
#         <neighbor name ="KARNATAKA" language ="Kannada"/>
#     </state>
#     <state name ="GUJARAT">
#         <rank>2</rank>
#         <neighbor name ="RAJASTHAN" direction ="N"/>
#         <neighbor name ="MADHYA PRADESH" direction ="E"/>
#     </state>
#     <state name ="KERALA">
#         <rank>3</rank>
#         <neighbor name ="TAMILNADU" direction ="S" language ="Tamil"/>
#     </state>
# </States>
# '''
# root = ET.fromstring(XMLexample_stored_in_a_string)
# for x in root.iter('neighbor'):
#     print(x.attrib)
