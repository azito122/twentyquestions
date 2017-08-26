import urllib.request
import re
from pprint import pprint

word = "moon"
html = urllib.request.urlopen("http://www.dictionary.com/browse/" + word + "?s=t")
html = str(html.read())
defs = re.findall('<meta name="description" content="(.*?)"\s*/?>',html,re.MULTILINE)

print(defs)