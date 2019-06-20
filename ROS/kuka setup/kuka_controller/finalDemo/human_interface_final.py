#!/usr/bin/env python

from client_final import *
from numpy import *
import time
from parserJsonMultiquery import *

#The function to prase the json data to strings.
def readJson(f):
    file = open(f,'r')
    
    jdson = str(file.read())
    jsonData = json.loads(jdson)
    queryPatterns = []
    for index in range(0,len(jsonData['actions'])):
        
        queryPattern = jsonData['actions'][index]['intent']['trigger']['queryPatterns']
        print(queryPattern)
        queryPatterns += queryPattern
    
    return (queryPatterns)

def function():
	pass