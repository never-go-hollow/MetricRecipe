#!/usr/bin/env python3

import re
from sys import argv
script, recipe_name = argv

multiplier = 1
loose = {'flour': '0.58', 'salt': '1.20', 'sugar': '0.84', 'yeast': '0.95', 'butter': '0.97', 'whipped cream': '0.5'}

class Convert(object):
    def __init__(self, pattern, number, unit, loose_unit):
        self.pattern = pattern
        self.number = number
        self.unit = unit
        self.loose_unit = loose_unit
    def convert_action(self):
        pattern = re.compile(self.pattern)
        matches = re.findall(pattern, line)
        digit = re.findall(r'(\d+)/?(\d+)?', line)
        if digit[0][1] != "":
            digit = float(digit[0][0])/float(digit[0][1])
        else:
            digit = float(digit[0][0])
        newline = re.sub(pattern, '', line)
        density = 1
        for word in loose:
            if word in newline:
                self.unit = self.loose_unit
                density = float(loose.get(word))
        converted = float('%0.1f' % (float(digit)*self.number*multiplier*density))
        for pattern in matches:
            print('['+ str(converted) + self.unit +']' + newline)

cup = Convert(r'(\d+)/?(\d+)?\s+(cups?)', 235, " ml", "g")
tablespoon = Convert(r'(\d+)/?(\d+)?\s+(tablespoons?|tbsp.?|tbsp?)', 14.7, " ml", "g")
teaspoon = Convert(r'(\d+)/?(\d+)?\s+(teaspoons?|tsp.?)', 4.9, " ml", "g")
pound = Convert(r'(\d+)/?(\d+)?\s+(pounds?|lbs?|lbs.?)', 0.45, " kg", "kg")
ounce = Convert(r'(\d+)/?(\d+)?\s+(ounces?|oz.?|oz?)', 28.34, " g", "g")

def read_file():
        with open(recipe_name) as file:
            data = file.read()
        return data.splitlines()
        
print('-'*8)
print('Servings?')
print('-'*8)
multiplier = int(input("> "))
print('-'*8)

for line in read_file():
    Convert.convert_action(tablespoon)
    Convert.convert_action(teaspoon)
    Convert.convert_action(pound)
    Convert.convert_action(ounce)
    Convert.convert_action(cup)
