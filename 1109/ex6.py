import os
import xml.etree.ElementTree as ET

cpath = os.getcwd()
fname = "ex5.xml"

tree = ET.parse(cpath+"/"+fname) #parser option빼면 기본 parser로 처리
root = tree.getroot()
print(root.tag)

for child in root:
    print("\t"+child.tag+":"+child.text)