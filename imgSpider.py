import urllib
import urllib2





def get_after(string,first,symbol="&quot;"):
 try:
  string+=" "
  start = string.index(first) + len(first)
  second = string.index(symbol,start)
  if second - start <= 1:
   second+= (1 if string[second + len(symbol)] == " " else 0)
   return string[second + len(symbol):string.index(" ",second+len(symbol))]
  else:
   return ""
 except ValueError:
  return ""





def image_type(pop):

 if ".GIF" in pop.upper():
  return ".gif"
 elif ".JPG" in pop.upper():
  return ".jpg"
 elif ".JPEG" in pop.upper():
  return ".jpg"
 elif ".PNG" in pop.upper():
  return ".png"
 elif ".WEBM" in pop.upper():
  return ".webm"









WHAT=raw_input("Enter term: ")
try:
 MANY =int(raw_input("How many?: "))
except:
 print ("Not a vaild number defaulting to 1")
 MANY = 1
response = urllib2.urlopen('http://www.bing.com/images/search?q='+WHAT)
html = response.read()
chunk = get_after(html,"imgurl:")

for i in range(0,MANY):
 url = chunk[:chunk.upper().find("&QUOT")]
 print url
 urllib.urlretrieve(url, WHAT+str(i)+image_type(url))
 chunk = get_after(html[html.index(chunk)+len(chunk):],"imgurl:")






