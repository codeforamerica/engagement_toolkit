#!/usr/bin/python

"""
Using the Likeminded API with CouchDB
"""

import urllib
from xml.dom import minidom
import sys
sys.path.append('/Users/UserName/Projects/engagement_toolkit/likeminded-python') #using the likeminded-python wrapper
import utils.xml2dict as xml2dict
import couchdb


BASE_URL = 'http://v1.api.likeminded.org/'
API_KEY = 'YOUR-API-KEY'
PAGE_NUMBER = '1'
ALL_PROJECTS_URL = BASE_URL + 'search/?apikey=' + API_KEY + '&type=Project' + '&page=' + PAGE_NUMBER

def getProjectList():
    idArray = []
    dom = minidom.parse(urllib.urlopen(ALL_PROJECTS_URL))
    results = dom.getElementsByTagName('results')[0]

    NUMBER_OF_RESULTS = results.getAttribute('available')
    NUMBER_OF_PAGES_TO_ITERATE = (int(NUMBER_OF_RESULTS) + 9) / 10 #10 results per page, integer division

    for i in range(1,NUMBER_OF_PAGES_TO_ITERATE+1):
        PAGE_NUMBER = i
        ALL_PROJECTS_URL1 = BASE_URL + 'search/?apikey=' + API_KEY + '&type=Project' + '&page=' + str(PAGE_NUMBER)
        dom = minidom.parse(urllib.urlopen(ALL_PROJECTS_URL1))
        projects = dom.getElementsByTagName('project') # returns an array
        j = 0
        for node in projects: 
            idArray.append(dom.getElementsByTagName('id')[j].firstChild.data)
            j = j + 1    
    getProjectDescription(idArray)
    
def getProjectDescription(idArray):
    j = 0
    description_list = []
    for i in idArray:
        PROJECT_ID = idArray[j]
        PROJECT_DESCRIPTION_URL = 'http://v1.api.likeminded.org/projects/' + PROJECT_ID + '?apikey=' + API_KEY
        RAW_XML = urllib.urlopen(PROJECT_DESCRIPTION_URL).read() #url open returns a file-like object; read returns the raw xml as a string
        CONVERTED_XML_TO_DICT = xml2dict.xml2dict(RAW_XML)
        description_list.append(CONVERTED_XML_TO_DICT)
        j = j + 1
    """
    #Get Output File
    FILE = open('output.txt',"w")
    #for name in description_list:
        FILE.write(str(description_list))
    FILE.close()
    """
    server = couchdb.Server('http://localhost:5984')
    db = server['lm_test']
    db.update(description_list, all_or_nothing=True)
getProjectList()