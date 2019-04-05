# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:31:43 2019

@author: user
"""
#
#import xlrd
#
#d = {}
#callLogsRec = xlrd.open_workbook('/C:/Users/user/AppData/Local/Temp/Temp1_GSH_19MAR2019.zip/FOR_UNCLASS/Phones (PARSED)/GSH_CallLogs.csv')
#callLogsexcel = callLogsRec.sheet_by_index(2)   
#for i in range(16347):
#    cell_value_number = callLogsexcel.cell(i,0).value
#    cell_value_name = callLogsexcel.cell(i,1).value
#    d[cell_value_number] = cell_value_name

#import csv
#
#with open('GSH_CallLogs.csv') as csvfile:
#    reader = csv.reader(csvfile)
#
#    mydict = {rows[0]:rows[1] for rows in reader}

import csv
with open('GSH_CallLogs.csv', newline = '', encoding = 'utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    data = [row for row in csv.reader(csvfile)]
    
    numbers = []
    for i in range(1,len(data)):
        numbers.append(data[i][0])
    print(numbers) 
        
    names = []
    for i in range(1, len(data)):
        names.append(data[i][1])
    print(names)
    
    call_num = []
    for i in range(1, len(data)):
        call_num.append(data[i][5])
    print(call_num)

    num_and_names = []
    for digit, alias in zip(numbers, names):
        num_and_names.append([digit, alias])
    print(num_and_names)
    
    mappedDictionary = dict(zip(call_num, num_and_names))
    print(mappedDictionary)
    
    
#            num_and_names.append([digit, alias])
#    print(num_and_names)
            
#            num_and_names = [digit, alias]
#    print(num_and_names)    
    
#    result = {}
#    for row in reader:
#        key = row[5]
#        if key in result:
#        # implement your duplicate row handling here
#            pass
#        result[key] = row[1:]
#    print(result)
#        
    
       