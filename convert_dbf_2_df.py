#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:58:47 2018

@author: eduardo
"""
#https://gist.github.com/ryan-hill/f90b1c68f60d12baea81
#https://www.files-conversion.com/file-convert/converted.php
#https://www.e-learn.cn/content/wangluowenzhang/283964

import pysal as ps
import pandas as pd
import dbf

'''
Arguments
---------
dbfile  : DBF file - Input to be imported
upper   : Condition - If true, make column heads upper case
'''
def dbf2DF(dbfile, upper=False): #Reads in DBF files and returns Pandas DF
    # Upper for the header
    db = ps.open(dbfile) #Pysal to open DBF
    d = {col: db.by_col(col) for col in db.header} #Convert dbf to dictionary
    #pandasDF = pd.DataFrame(db[:]) #Convert to Pandas DF
    pandasDF = pd.DataFrame(d) #Convert to Pandas DF
    if upper == True: #Make columns uppercase if wanted 
        pandasDF.columns = map(str.upper, db.header) 
    db.close() 
    return pandasDF
    

    
if __name__ == "__main__":
    
    '''
        Load .dbf into DataFrame
    '''
    df = dbf2DF('test.dbf')
    
    '''
        Save DF into .CSV
    '''
    df.to_csv('test.csv',index=None)
    
    '''
        Load CSV
    '''
    csv_file = dbf.from_csv(csvfile='test.csv', to_disk=True) 
    
    
    