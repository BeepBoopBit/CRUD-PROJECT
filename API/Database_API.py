from dataclasses import dataclass
import MySQLdb

class Database:
    def __init__(self, userName, userPassword) -> None:
        self.db = MySQLdb.connect(
            host="localhost",
            user=userName,
            password=userPassword
        )
        self.cursor = self.db.cursor()
    #######################################################
    # Use Functions    
    def useDatabase(self, dbName):
        self.cursor.execute(f"USE {dbName}")    
        
    # Getters Function
    def getDatabase(self):
        return self.db
    
    def getDatabaseList(self):
        self.cursor.execute("SHOW DATABASES");
        return self.cursor;
    
        
    #######################################################
    
    # Debugging Purposes
    def Print_Database(self):
        self.cursor.execute("SHOW DATABASES;")
        print(type(self.cursor));
        for x in self.cursor:
            print(x)
