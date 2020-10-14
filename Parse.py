import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
for child in root.iter('param'):
    print ([i for i in child.attrib.values()])
for child in root.iter('param'):
    print (child.attrib)
