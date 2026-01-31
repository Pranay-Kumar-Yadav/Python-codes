#XML Processing
import xml.dom.minidom

domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

persons = group.getElementsByTagName('persons')

for person in persons:
    print("-----PERSON-----")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute('id')))

    print("Name: {}".format(person.getElementsByTagName('Name')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('Age')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('Weight')[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName('Height')[0].childNodes[0].data))

    newperson = domtree.createElement('person')
    newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Paul Green'))

Age = domtree.createElemnt('age')
age.appendChild(domtree.createTextNode('19'))

name = domtree.createElement('weight')
name.appendChild(domtree.createTextNode('80'))

name = domtree.createElement('height')
name.appendChild(domtree.createTextNode('179'))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)

domtree.writexml(open('data.xml', 'w'))