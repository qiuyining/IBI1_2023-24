# Import necessary libraries
import matplotlib.pyplot as plt
from datetime import datetime

# Using DOM
import xml.dom.minidom
#record the time before DOM processing the file
start_time_DOM = datetime.now()
# Parse the XML file
DOMTree = xml.dom.minidom.parse("D:/IBI/IBI_git/IBI1_2023-24/Practical14/go_obo.xml")
# Get the root element of the document
collection = DOMTree.documentElement
# Find all 'namespace' elements
namespace = collection.getElementsByTagName('namespace')
interested_namespaces = ['molecular_function', 'biological_process', 'cellular_component']
# Initialize a dictionary to store the count of each namespace
total={}
# Count the namespaces
for name in namespace:
    name_text =  name.firstChild.nodeValue
    if name_text in interested_namespaces:
        if name_text not in total:
            total[name_text] = 1
        else:
            total[name_text] += 1
print(total)
#record the time after DOM processing the file
end_time_DOM = datetime.now()
# Calculate the taken time
time_taken_DOM = end_time_DOM - start_time_DOM
print(f"The time taken to parse XML using DOM is {time_taken_DOM}")

# Show the bar chart
plt.bar(total.keys(), total.values(), width=0.5)
plt.xlabel('ontology')
plt.ylabel('the number of terms')
plt.title('the number of terms within each ontology')
plt.xticks(rotation=90) 
plt.tight_layout()
plt.show()
plt.clf()

# Using SAX
import xml.sax
#record the time before SAX processing the file
start_time_SAX = datetime.now()
#Create a SAX parser
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# List to store the namespace values
namelist=[]
# Reset the dictionary for SAX counts
total={}
# Set the handler 
class namespaceHandler (xml.sax.ContentHandler):
    #initialize the values
    def __init__(self):
        self.currentElement = ''
        self.namespace=''

    def startElement(self, tag, attrs):
        self.currentElement = tag

    def characters(self, content):
        if self.currentElement == 'namespace':
            self.namespace += content.strip()

    def endElement(self, tag):
        if tag == 'namespace':
            if self.namespace:  
                namelist.append(self.namespace)  
                self.namespace = ''  

# Create an instance of the handler
handler = namespaceHandler()
# Set the content handler for the parser
parser.setContentHandler(handler)
# Parse the XML file using the SAX parser
parser.parse("D:/IBI/IBI_git/IBI1_2023-24/Practical14/go_obo.xml")

# Count the namespaces
for name in namelist:
    if name in interested_namespaces:
        if name not in total:
            total[name] = 1
        else:
            total[name] += 1
print(total)

#record the time after SAX processing the file
end_time_SAX = datetime.now()
# Calculate the taken time
time_taken_SAX = end_time_SAX - start_time_SAX
print(f"The time taken to parse XML using SAX is {time_taken_SAX}")

# Show the bar chart
plt.bar(total.keys(), total.values(), width=0.5, color='green')
plt.xlabel('ontology')
plt.ylabel('the number of terms')
plt.title('the number of terms within each ontology')
plt.xticks(rotation=90) 
plt.tight_layout()
plt.show()
plt.clf()

# The time taken to parse XML using DOM is 0:00:08.458981.
# The time taken to parse XML using SAX is 0:00:01.341930.
# SAX is quicker.