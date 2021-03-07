import pandas as pd
import numpy as np
import tushare as ts

import json
import sys

from storeOps import SQLserverOperator


#Processing argv
if len(sys.argv) < 3:
    print('Both source and desination configuration required')
    exit(1)

with open(sys.argv[1], 'r') as load_f:
    srcConfig = json.load(load_f)

#Extract data
pro = ts.pro_api(srcConfig['tushare'])

fields = ['ts_code','symbol','name,area','industry','fullname','enname','market','exchange','curr_type','list_status'
            ,'list_date','delist_date','is_hs']
data = pro.stock_basic(exchange='', list_status='L', fields=','.join(fields))

#Cleaning
data.loc[data['delist_date'].isnull(), 'delist_date'] = '99991231'

#Load data
opr = SQLserverOperator(sys.argv[2])
opr.loadDF('stock_name', data)
del opr