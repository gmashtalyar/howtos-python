import xml.dom.minidom

domtree = xml.dom.minidom.parse("10_data.xml")
group = domtree.documentElement

persons = group.getElementsByTagName('person')

for person in persons:
    print("-----PERSON-----")
    if person.hasAttribute("id"):
        print(f"ID: {person.getAttribute('id')}")

    print(f"Name: {person.getElementsByTagName('name')[0].childNodes[0].data}")
    print(f"Age: {person.getElementsByTagName('age')[0].childNodes[0].data}")
    print(f"Weight: {person.getElementsByTagName('weight')[0].childNodes[0].data}")
    print(f"Height: {person.getElementsByTagName('height')[0].childNodes[0].data}")


# persons[2].getElementsByTagName("name")[0].childNodes[0].nodeValue = "New Name"
# persons[0].setAttribute("id", "100")
# persons[3].getElementsByTagName("age")[0].childNodes[0].nodeValue = "-10"
# domtree.writexml(open("10_data.xml", "w"))

newperson = domtree.createElement("person")
newperson.setAttribute('id', "6")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Paul Green"))
age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("30"))
weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("80"))
height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("179"))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)

domtree.writexml(open("10_data.xml", "w"))
