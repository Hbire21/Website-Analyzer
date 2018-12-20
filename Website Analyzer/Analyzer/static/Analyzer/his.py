import urllib2
response = urllib2.urlopen('http://tinyurl.com/5b2su2')
if response.geturl():
    print response.geturl()
else:
    print "nope"
url = "https://www.google.com/"
req = urllib2.urlopen("https://www.google.com/")
req = urllib2.Request(url=url)
resp = urllib2.urlopen(req, timeout=3)
redirected = resp.geturl() != url # redirected will be a boolean True/False
if redirected:
    print redirected
else:
    print "false"



from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://google.com")

# This will get the initial html - before javascript
html1 = driver.page_source

# This will get the html after on-load javascript
html2 = driver.execute_script("return document.documentElement.innerHTML;")
print html2