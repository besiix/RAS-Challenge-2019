#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:53:54 2019

@author: wuchenhao
"""
import json

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

queryPatterns = readJson('team2v2.json')

