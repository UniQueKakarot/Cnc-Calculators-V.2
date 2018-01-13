import openpyxl as pyxl
from openpyxl import Workbook
from openpyxl import load_workbook
import os
import os.path


class FileHandling():
    
    def checkfile(self, data):
        
        """ Method for checking if the file exists and if not, generate new """
        
        if os.path.isfile(data) is True:
            pass
        else:
            wb = Workbook()
            wb.save(data)


class CuttingSpeedData():
    
    def __init__(self, data):
        self.data = data
        
        self.wb = load_workbook(self.data)
        
        test = 0
        
        for i in self.wb.get_sheet_names():
            if i == "Cutting Speed":
                test = 1
                
        if test == 0:
            self.ws = self.wb.create_sheet("Cutting Speed")
            x = self.wb.get_sheet_by_name('Sheet')
            self.wb.remove_sheet(x)
            
            ws = self.wb["Cutting Speed"]
            ws.cell(row=2, column=2, value="Cutting Meter")
            ws.cell(row=2, column=3, value="Mill Diameter")
            ws.cell(row=2, column=4, value="Number of teeth")
            ws.cell(row=2, column=5, value="Feed pr Tooth")

        self.wb.save(self.data)
    
    def cutting_meter(self, cuttingdata, mill, teeth, tooth):
        
        ws = self.wb["Cutting Speed"]
        
        if os.path.isfile("Usefulldata.txt") is True:
            with open("Usefulldata.txt", "r") as f:
                row = f.readline()
            row = int(row)
        else:
            row = 3
        
        try:
            cuttingdata = int(cuttingdata)
        except ValueError:
            pass
        try:
            mill = int(mill)
        except ValueError:
            pass
        try:
            teeth = int(teeth)
        except ValueError:
            pass
        try:
            tooth = float(tooth)
        except ValueError:
            pass
        
        ws.cell(row=row, column=2, value=cuttingdata)
        ws.cell(row=row, column=3, value=mill)
        ws.cell(row=row, column=4, value=teeth)
        ws.cell(row=row, column=5, value=tooth)
        row += 1
        
        self.wb.save(self.data)
        
        if os.path.isfile("Usefulldata.txt") is True:
            os.remove("Usefulldata.txt")
        
        row = str(row)
        with open("Usefulldata.txt", "w") as f:
            f.write(row)
            