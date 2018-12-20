# Website-Analyzer
Analyzes Website source code and stores the details in database and show for user.


## Pre conditions 

Install the following packages

    $pip install django

    $pip install selenium 

    $pip install requests

    $pip install Beautifullsoup


## Getting Started 

Type below comand on your comman line, choose any port you want

    $ python manage.py runserver [port number]


## Project final Plan

New words inside the document and their meanings


## introduction 

Attackers lure an unsuspecting victim to visit malicious websites and they steal important credentials from the victim or install malware on the victim's machine to use it as a springboard for future exploits. When the victim visits a malicious website, the attack is initiated and up on finding evidences of exploitable vulnerabilities (e.g., of browser components, of browser extensions), the attack payload is executed. Detection mechanisms have been developed since this problem detected. Most people who work in the anti-malware industry are familiar with signature-based detection, where if a file is determined to be malicious, a signature is written so anti-malware programs are able to detect that file or component in the future. As opposed to this method W.M.A uses both rule based and signature based detection methods.

# Functonality 

## Features 

  #### Detection
  #### Prediction 
  #### Real-time 

### Detection 

#### W.M.A Detection Functionalities                              

#### W.M.A Extraction Functionalities 

### Prediction 

Configuring X-frame header helps to protect a website from clickjacking “Clickjacking (UI redressing attack)  is when an attacker uses multiple transparent or opaque layers to trick a user into clicking on a button or link on another page when they were intending to click on the the top level page.”  Source: Owasp
Discovering that the website has no protection against this attack would be the first thing to do and prediction relies here : let’s declare that there is a website W, there are different possible mitigation methods M1, M2, M3, ……..

Scenario - If W has protection against clickjacking 
it could be either frame buster or X-frame Options, “as frame busters are hacks. Nasty messy hacks of limited efficiency.
what we really need is a simpler, more semantic means of specifying how and where a page may be used when it comes to being embedded in a frame and that's what we have in the X-Frame-Options (XFO) header.” source Troy Hunt. Based on this state

### Declaration 

```python
M1 = X-FRAME-OPTIONS HTTP response header
M1.values = {DENY, SAMEORIGIN, ALLOW-FROM}
   ```
### Condition 

```python
  If W has (M1 set to M1.values [1]) :
  M1.values [1] checks if a parent page is from the same domain as your site page
  call Result
  else:
  W have no protection against clickjacking attack                          
  //Result      
  W satisfied protection of  clickjacking attack 
   ```
                                 
Tip : - Detection involves crawling through given url content and by looking for possible urls using automated google search engine.
Real-time
The detection performed by collecting resources of client side W resources. 

### URL-Based 

Malicious URL or  malicious website, is a common and serious threat to cybersecurity. Malicious URLs host unsolicited content (spam, phishing, drive-by exploits, etc.) and lure unsuspecting users to become victims of scams (monetary loss, theft of private information, and malware installation), and cause losses of billions of dollars every year. It is imperative to detect and act on such threats in a timely manner. Source- A survey
In this section, W.M.A perform analysis on any urls that it may have encountered.


### Automated Google search feature

```python do 
{
            U input http://www.example.com W.MA request google search engine for the url and 
                                                  Automated Google search
                                                                        then 
                                           W.M.A extracted possible related urls 
                                                                       then 
                                                Automated Google search feature 
}
 
```
         
Given url analysis

Tested against X-FRAME option mitigation enable detection , Phishing Address Bar Based features, Google safe browsing blacklist.

Scenario 
              
```python 

if U give a valid url
do
 {
crawling through content involves all links which starts by given website url
and
 Automated Google search
}

call X-FRAME option mitigation enable detection_func  and call Address Bar based features_func()  and call Google safe browsing blacklist_func   
```

### Redirected url analysis 
A URL Redirection Attack is a kind of vulnerability that redirects you to another page freely out of the original website when accessed, page could lead to a malicious page that resembles the original, and tries to trick the user into giving their credentials. Source - Paralliverse
Get the final redirected url and test against X-FRAME option mitigation enable detection , Phishing features, Google safe browsing blacklist.


Scenario 

if U give a valid url that have a redirection capability.
W.M.A get the final redirected url or possible url that can be visited by U and perform
url_analysis.

```python 

def url_analysis()
{
do 
{
     crawling through content involves all links which starts by given website url
and
 Automated Google search
}
call X-FRAME option mitigation enable detection_func and call Address Bar based features_func()  and call Google safe browsing blacklist_func 
}

```

### Invalid url analysis 
Invalid url When you conduct Internet research into products, competitors, clients and prospects, you use Uniform Resource Locators, or URLs, to locate the online destinations of the information you want to evaluate. Enter an invalid URL and your browser software displays a warning that the website or page you want to view doesn't exist. Distinguishing incorrect entries from those that really don't point to valid sites or pages can help you correct your entries and finish your research. Example Mistyped, Incomplete, Nonexistent, Invalid Characters. Source- Chron
If U give an invalid url W.M.A validate the url using  google shortener behavior, redirected url.

Scenario 

if U give an invalid url.

```python

do
{
if  the url use google url shortener
unshorten the url()
call url_analysis()
else
alert(invalid url)
}
url_analysis()
{
do
 {
crawling through content involves all links which starts by given website urls
and
                                                 Automated Google search
}
call X-FRAME option mitigation enable detection_func  and call Address Bar based features_func()  and call Google safe browsing blacklist_func 
}
```

## Sample phishing features 
Phishing is an online criminal act that occurs when a malicious web page impersonates as legitimate webpage so as to acquire sensitive information from the user. Phishing attack continues to pose a serious risk for web users and annoying threat. Source Springer Open
Address Bar features

scenario 

```python 
if domain part has ip address or obfuscated code and has  long url to hide suspicious behaviour of the website 
 {
then

 Call add_suspecious_behaviour() 
 
 else
 
Call add_clean_behaviour()   

}
```

## HTML tag analysis and JavaScript analysis 
Html tag analysis 

Meta tag redirection 
What to look for

    meta http-equiv="refresh" content="0";
    url=http://www.YourOwnDomainNameHere


    Check the length of the redirection url
    Check redirection to external web resource


Iframe tag redirection 
    What to look for

<iframe src=”hxxp://evil.site/count.php?o=1″ width=0 height=0 style=”hidden” frameborder=0 marginheight=0 marginwidth=0 scrolling=no></iframe>


JavaScript analysis
 What to look for
 
iframe redirection 
Pop up window have text fields

## Deobfuscation 

Obfuscation is a means of "obscuring" the real meaning and intent of your javascript code. Some sites use it as an obstacle to people who want to copy/borrow their code. Other sites use it as a means to hide the actual intention of the code.
Some forms of obscuration:
Automatically renaming variables to short meaningless names to make the code less readable and harder to understand.
Removing all extra whitespace and line breaks so the code is one giant long line.
Making parts of the code self-generating so that a first pass of the code runs to create the actual code that then runs to carry out the intended operation.
Uses character codes and string manipulation combined with eval rather than normal javascript code to construct the actual code that would run. Source- StackOverflow
Deobfuscate javascript code means make the code readable so that W.M.A investigate further. 

## Content Based
W.M.A crawl through urls that it encountered during the scanning process and check if any links parameter “src=” and the website have different domain names.
include html tag analysis under phishing attack features   and  url based analysis

## unique features
                  
This analyzer doesn’t care about the validity of a url, analyze any url given to it.    
Not only crawl through given url content also open links associated with it.    
Use automated Google search technique.
         
Techniques used 

    Data extraction
    Built in parsers, string based analysis (e.g split).
    Detection
    phishing Website Features
    check for blacklist
    Signature-based matching a few 

Development

    python programing language
    django framework
