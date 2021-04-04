#SimplePython
#Designed and programmed by thepiger4009 in python
#Made on Linux Mint, and designed for linux.

#Import Modules
from os import system
import time
import random
#---

#Display, that the program using this module uses SimplePython
print("SimplePython v1.0")
print("Hello from SimplePython, @2021")
print("")
#---

def say(string):
    print(string)
    
def add(variableNumber,variableNumber2):
    product = variableNumber + variableNumber2
    return product
    
def sub(variableNumber,variableNumber2):
    product = variableNumber - variableNumber2
    return product

def multiply(variableNumber,variableNumber2):
    product = variableNumber * variableNumber2
    return product
    
def ask(string):
    product = input(string)
    return product

def askNum(string):
    product = int(input(sting))
    return product

def makeList(legnth):
    vlist = [1] * legnth
    return vlist

def compare(variable1,variable2):
    if variable1 == variable2:
        state = "True"
    else:
        state = "False"
    return state




    