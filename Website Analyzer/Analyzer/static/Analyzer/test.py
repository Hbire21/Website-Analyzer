
import datetime
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
from bs4 import BeautifulSoup
soup = BeautifulSoup("http://127.0.0.1:8004/Analyzer/Scan")
#print(soup)
from selenium import webdriver
#driver = webdriver.Firefox()
#driver.get("http://127.0.0.1:8004/Analyzer/Scan")
#driver.execute_script('document.title')
#result = driver.execute_script('var text = document.title ; return var')
#print result

from bs4 import BeautifulSoup
import requests
#soup = requests.get("https://www.google.com/search?client=ubuntu&channel=fs&q=Could+not+find+a+version+that+satisfies+the+requirement+PyQt4+%28from+versions%3A+%29No+matching+distribution+found+for+PyQt4&ie=utf-8&oe=utf-8")
#c = soup.content
#soup = BeautifulSoup(c, "html.parser")
#g = soup.find('p')
#print g
import json
#https://stackoverflow.com/jobs?med=site-ui&ref=jobs-tab&sort=p
from bs4 import BeautifulSoup
import requests
link = 'https://stackoverflow.com/questions/31624041/print-n-or-newline-characters-as-part-of-the-output-on-terminal'
r = requests.get(link)
soup = BeautifulSoup(r.text, 'html.parser')
s = soup.find_all('script')
for a in s:
    print "result"
    print(a.text)
#print "source codxe"
#print soup



import urllib2

request = urllib2.Request("http://www.paperbackswap.com/mobile/index.php?ti=python")
response = urllib2.urlopen(request)
the_page = response.read()
theText = the_page.decode()
# print theText
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import html5lib

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get('https://stackoverflow.com/questions/23302769/python-selenium-switch-into-an-iframe-within-an-iframe')
try:
    time.sleep(4)
    iframe = driver.find_elements_by_tag_name('iframe')[0]
    driver.switch_to.default_content()

    driver.switch_to.frame(iframe)

    driver.find_elements_by_tag_name('iframe')[0]

    output = driver.page_source

    print output

finally:
    driver.quit();
"""

from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor


data = """
$.ajax({"@context":"http:\/\/schema.org","@type":"WebSite","@id":"#website","url":"http:\/\/iwtc.info\/","name":"IWTC","potentialAction":{"@type":"SearchAction","target":"http:\/\/iwtc.info\/?s={search_term_string}","query-input":"required name=search_term_string"}}
);
"""

parser = Parser()
tree = parser.parse(data)
fields = {getattr(node.left, 'value', ''): getattr(node.right, 'value', '')
          for node in nodevisitor.visit(tree)
          if isinstance(node, ast.Assign)}
#print fields


from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast
parser = Parser()
tree = parser.parse('for(var i=0; i<10; i++) {var x=5+i;}')
for node in nodevisitor.visit(tree):
    if isinstance(node, ast.Identifier):
        print node.value



