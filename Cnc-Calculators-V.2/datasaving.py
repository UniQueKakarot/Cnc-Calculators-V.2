import openpyxl as pyxl
from openpyxl import Workbook
import os.path


class FileHandling():
    
    def checkfile(self):
        
        """ Method for checking if the file exists and if not, generate new """
        
        if os.path.isfile('Database.xlsx') is True:
            return True
        else:
            wb = Workbook()
            wb.save('Database.xlsx')

class CuttingSpeedData():
    
    def filegen(self):
        pass