import pandas as pd
import pyodbc as pdc
import numpy as np
import json


class SQLserverOperator:

    def __init__(self, configFile):
        with open("configFile", 'r') as load_f:
            config = json.load(load_f)
        
        if config['AuthType'] == 'SQLserver':
            connStr = 'DRIVER={SQL Server};SERVER=' + config['server'] + ';DATABASE=' + 
                        config['database'] + ';UID=' + config['username'] + ';PWD='+ config['password']
            
        self.conn = pdc.connect(connStr)

    def __del__(self):
        self.conn.close()
        

    def loadDF(self, table, data):
        cursor = self.conn.cursor()

        for item in data.values:
            try:
                cursor.execute("INSERT INTO " + table + " VALUES(" + ','.join(item) + ")")
            except:
                print("Row " + item[0] + " Error:", err)
        