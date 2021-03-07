import pyodbc as pdc
import json


class SQLserverOperator:

    def __init__(self, configFile):
        with open(configFile, 'r') as load_f:
            config = json.load(load_f)
        
        if config['AuthType'] == 'SQLserver':
            server = config['server']
            database = config['database']
            username = config['username']
            password = config['password']

            connStr = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

        self.conn = pdc.connect(connStr)

    def __del__(self):
        self.conn.close()
        

    def loadDF(self, table, data):
        cursor = self.conn.cursor()

        for item in data.values:
            try:
                cursor.execute("INSERT INTO " + table + " VALUES(" + ','.join(['?']*len(item)) + ")", tuple(item))
            except Exception as err:
                print(item[0] + "::", str(err))

        self.conn.commit()
        cursor.close()