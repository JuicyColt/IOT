import xml.etree.ElementTree as ET
import random

root = ET.Element('data')

params = ET.SubElement(root,'params')

air_humidity = ET.SubElement(params,'param',name='air_humidity',
                             value = f'{random.uniform(4.8,100):.1f}')

temperature = ET.SubElement(params,'param', name='temperature',
                            value = f'{random.uniform(-5,25):.0f}')
#ET.dump(root)
for method in [ 'xml', 'html']:
    ET.ElementTree(root).write(f"data.{method}",
                           xml_declaration=True,
                           encoding='UTF-8',
                               method = method)
