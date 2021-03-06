import pandas as pd
import numpy as np
import pyodbc as pdc
import tushare as ts


def insertRow(row):
    

#Extract data
pro = ts.pro_api('420d07dce1b7c0641907e87dcd90d3d0e08250b4d45f65e2de909ca8')

fields = ['ts_code','symbol','name,area','industry','fullname','enname','market','exchange','curr_type','list_status'
            ,'list_date','delist_date','is_hs']
data = pro.stock_basic(exchange='', list_status='L', fields=','.join(fields))

#Load data
server = '112.242.85.71' 
database = 'inst_test' 
username = 'sa' 
password = 'wasd3695' 
connStr = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

conn = pdc.connect(connStr)
cursor = conn.cursor()

