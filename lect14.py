from xml.etree import ElementTree as et

root = et.Element('tasks')
day = et.SubElement(root, 'day')
day.set('date', '01.01.2018')

task1 = et.SubElement(day, 'task')
task2 = et.SubElement(day, 'task')

task1.text = 'WakeUp'
task2.text = 'Make coffee'
tree = et.ElementTree(root)
tree.write('tasks.xml')

tree = et.parse('tasks.xml')
tree.findall('.')
for el in tree.findall("day[@date='01.01.2018']//task"):
    print(el.text)

print(tree.getroot()[0])
print(tree.getroot()[0][0])

##############################################

'''DOM parcer'''

from xml.dom import minidom

tree = minidom.parse('tasks.xml')
print(dir(tree))
print(tree.firstChild)
print(tree.firstChild.firstChild)
print(tree.firstChild.firstChild.childNodes)
for el in tree.firstChild.firstChild.childNodes:
    print(el.firstChild.wholeText)

##############################################

'''StAX parcer'''

from xml.dom import pulldom

doc = pulldom.parse('tasks.xml')
for event, node in doc:
    if event == pulldom.START_ELEMENT and node.localName == 'task':
        doc.expandNode(node)
        print(node.firstChild.wholeText)

##############################################

'''SAX parcer'''

from xml import sax


class TasksHandler(sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.is_task = False

    def startElement(self, name, attrs):
        if name == 'task':
            self.is_task = True

    def endElement(self, name):
        if name == 'task':
            self.is_task = False

    def characters(self, content):
        if self.is_task:
            print(content)

parser = sax.make_parser()
parser.setContentHandler(TasksHandler())
parser.parse(open('tasks.xml', 'rt'))
