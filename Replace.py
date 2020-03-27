import re

with open('/home/blueberrykary/ourfirstscraper/plist', 'r') as my_file:
    text = my_file.read()
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("*", "")
    text = text.replace("+", "")
    text = text.replace(".", "")   
    
    text = re.sub("\d+", " ", text)

# Created new file to replace previous list
with open('/home/blueberrykary/ourfirstscraper/replace1.txt', 'w') as my_file:
    my_file.write(text)
