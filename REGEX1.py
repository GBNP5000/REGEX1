from bs4 import BeautifulSoup
import requests
import re

#url ="https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fui%3Dhtml%26zy%3Dl&bsv=1eic6yu9oa4y3&ss=1&scc=1&ltmpl=default&ltmplcache=2&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

#r  = requests.get(url)

#FILE - OPERATION
F1 = open ("D:/PYTHONS/REGEXFI.txt","r")
data = F1.read()

soup = BeautifulSoup(data,"html5lib")

F1.close()
print(data)
print("")
print("")
d1 =  re.sub('((?:(?<=\[))https?://(?:[\-\w.]|(?:[\da-zA-Z0-9\.\%\/\&-_])*)\.[A-Z0-9a-z\/\?\=_]*)(?:\]).*(?<=\])([A-Za-z\.\&\(\)\%0-9\?\=_]*)' ,'<a href=\"\\1\">\\2</a>', (data))


#d2 =  re.sub('\[(https?://.*(?=\]))|\](.*\\n)', '<a href=\"\\1\">\\2</a>', (data))
print("AFTER  RE.SUB WITH WHOLE DATA ")
print("my REGEX \n\n %s " %d1)
print("")
#print("")
#print("fb  REGEX  %s " %d2)
