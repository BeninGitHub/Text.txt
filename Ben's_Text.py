#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 19:30:42 2021

@author: bnzr
"""


def revword(word):
    i=len(word)
    newstring= " "
    while i>0:
        i =i-1
        newstring = newstring + word[i]
    return newstring.lower() 

def countword()->int:    
    file= open('text.txt')
    line1 = file.readline()
    counter=0
    for line in file:
        line=line.rsplit()
        for word in line:
            word= revword(word)  
            if word in line1:
               counter= counter+1
    return(counter)       
                

