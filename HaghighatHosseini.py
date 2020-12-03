#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 08:05:03 2020

@author: mojdeh
"""

def int_to_roman(number):
    roman_result = ""
    #define a 2D List for distinguishing Tens, Hundreds, Thousand
    roman_numeral = [
        
                        ['','I','II','III','IV','V','VII','VII','VIII','IX'],
                        ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
                        ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
                        ['','M','MM','MMM']
        
        
               ]
    # i is a counter that determine the row in which the roman number exists
    i = 0  
    #doing Sequential division and considering remainders as internal elemets of each row
    while (number/10 != 0):
        remainder = int(number%10)
        number = int(number/10)
        #find new letter and join it to letters finding it previous steps
        roman_result = roman_numeral[i][remainder]+roman_result
        i=i+1
    #after quotient become zere, our woek is done    
    return(roman_result)    

int_to_roman(794)    

def roman_to_int(roman_number):
    
    result = 0
    #defining each letter in Roman number as an int number in a dictionary
    int_dict = {
                    'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000
        
                }
    
    #considering Roman number as a string
    for i in range(0,len(roman_number)-1):
        #because of substractive notation with 4,9,40,90,400,900 values, we should compare two letters wich are next te each other
        if int_dict[roman_number[i]]>=int_dict[roman_number[i+1]]:
            result=result + int_dict[roman_number[i]]
        else: 
            result=result+int_dict[roman_number[i+1]]-int_dict[roman_number[i]]
            
    return(result)


#call functions
print(roman_to_int('XXXIX'))
print(int_to_roman(roman_to_int('XXXIX')))
   
             
            
        
        