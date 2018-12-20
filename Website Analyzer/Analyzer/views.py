# -*- coding: utf-8 -*-
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.generic import View
from selenium import webdriver

import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

#home class
class HomeView(View):
    def get(self,request):
        return render(request, 'Analyzer/home.html', {'current_time':current_time})

#user scan class
class ScanView(View):

    #  get from form

    def get(self, request):
        query1 = request.GET.get('query')
        val = URLValidator()
        if query1 is None:  # check for empty form submit
            return render(request, 'Analyzer/user scan.html')
        else:
            try:
                val(query1)
                soup = requests.get(query1)
                c = soup.content
                soup = BeautifulSoup(c, "html.parser")
                return render(request, 'Analyzer/user scan.html')
            except ValidationError, e:
                return render(request, 'Analyzer/404.html')


#technical user info class
class Tech(View):

    #  get from form

    def get(self, request):
        query1 = request.GET.get('query')
        val = URLValidator()
        if query1 is None:  # check for empty form submit
            return render(request, 'Analyzer/Tech scan.html')
        else:
            try:
                val(query1)
                soup = requests.get(query1)
                c = soup.content
                soup = BeautifulSoup(c, "html.parser")
                samples = soup.prettify().encode('utf-8')
                div_containers = soup.find_all('div')
                link_a = []
                so = soup.find_all('a')
                for a in so:
                    so = a.get('href')
                    link_a.append(so)
                # ifr_len = len(ifr)
                # script_len = len(script)

                content_len = len(samples)
                div_len = len(div_containers)

                # script tag content info
                r = requests.get(query1)
                soup = BeautifulSoup(r.text, 'html.parser')
                script_info = soup.find('script')
                scriptdata = script_info.text




                # script tag info
                script = []
                links = soup.find_all('script')
                for link in links:
                    scripts = link.get("src")
                    script.append(scripts)


                # iframe tag info
                i_link = []
                i_links = soup.find_all('iframe')
                for i_link in i_links:
                    i_links = i_link.get("src")
                    i_link.append(i_links)
                # now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

                # script content
                #for a in links:
                    #s_content = a.text

                #execute document.title javscript
                #driver = webdriver.Firefox()
                #driver.get(query1)
                #driver.execute_script('document.title')
                #result = driver.execute_script('var text = document.title ; return var')



                return render(request, 'Analyzer/Tech scan.html',
                              dict(query1=query1, scripts=script, i_links=i_link, link_a=link_a,
                                   content_len=content_len, so=so, current_time=current_time,
                                   script_data=scriptdata))


            except ValidationError, e:
                return render(request, 'Analyzer/404.html')
