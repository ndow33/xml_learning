import os
from xml.etree import ElementTree

filename = 'reed.xml'
full_file = os.path.abspath(os.path.join('data', filename))

dom = ElementTree.parse(full_file)


courses = dom.findall('course')

for c in courses:
    title = c.find('title').text
    num = c.find('crse').text
    days = c.find('days').text

    print(f' * {num} [{days}] {title} ')

