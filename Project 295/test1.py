#Regular Expression
import re
k="The rain in Spain"

x=re.search("^The.*Spain$",k)   #.* will tell whether words are there in btw or not
if(x):
    print("yes")
else:
    print("No Match")