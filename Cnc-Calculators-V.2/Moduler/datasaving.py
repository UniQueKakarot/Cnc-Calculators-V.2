import openpyxl as pyxl
from openpyxl import Workbook
import os.path


class FileHandling():
    
    def checkfile(self, data):
        
        """ Method for checking if the file exists and if not, generate new """
        
        if os.path.isfile(data) is True:
            return True
        else:
            wb = Workbook()
            wb.save(data)
            return False

class CuttingSpeedData():
    
    def filegen(self):
        pass