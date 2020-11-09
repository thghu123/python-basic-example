import os
from xml.etree.ElementTree import Element,dump,SubElement,ElementTree

personal = Element('personal') #personal이라는 엘리멘트 생성
#personal에 들어갈 name과 phone이라는 element 만든다.

name = Element("name")
phone = Element("phone")

name.text = "마루치"
phone.text = "01020421234"

personal.append(name)
personal.append(phone)

SubElement(personal,'addr',p_no='098654').text = "서울시"

#dump는 화면 출력 용

dump(personal)

cpath = os.getcwd() #현재 경로
f_name = "ex5.xml"
ElementTree(personal).write(cpath +"/"+f_name,encoding="utf-8",xml_declaration=True)
#xml 문서가 만들어졌다.
#ex6은 파싱