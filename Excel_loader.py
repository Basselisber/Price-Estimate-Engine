import openpyxl as xl
from Column import *
import pandas as pd
import random



class Excel_Loader:
    sheet_names = []

    def __init__(self):
        pass

    def load(self, file_name):
        workbook = xl.load_workbook(file_name)
        sheets = workbook.sheetnames
        for sheet in sheets:
            self.sheet_names.append(sheet) # add sheet name to sheet_names list as the variable to load in other class ask question
        print("File loaded successfully")
        print("Sheet names: ", self.sheet_names)
        all_entities = []
        for name in self.sheet_names:
            print(name)
            x = self.load_sheet(workbook, name)
            all_entities.append(x)
        return all_entities


    def load_sheet(self, workbook, sheet_name):
        current_sheet = workbook[sheet_name]
        entity = Entity(sheet_name)
        column_name = ['name','manufacturer','year','price']
        first = True
        for row in current_sheet.rows:
            if first == True:
                first = False
                continue
            index = 0
            for cell in row:
                entity.get_column(column_name[index]).add_value(cell.value)
                index += 1
        return entity
            
class Data_Generator:
    def __init__(self):

        self.df = pd.DataFrame()
        self.column_names = ['name','manufacturer','year','price']
        for col in self.column_names:
            if col== 'name' or col == 'manufacturer':
                self.df[col] = pd.Series(dtype='str')
            elif col == 'year':
                self.df[col] = pd.Series(dtype='int')
            else:
                self.df[col] = pd.Series(dtype='int')
        
    def generate_data(self, num_rows,loader,entities):
        for i in range(num_rows):
            rand_col = random.choice(loader)
            idx = loader.index(rand_col)
            x = entities[idx].get_column('name').get_values()
            random_name = random.choice(x)
            self.df.loc[i,'name'] = random_name
            print(self.df)


loader = Excel_Loader()
entities = loader.load('Price-Estimate-Engine/data/data-bassel.xlsx')
all_dat = Data_Generator()
all_dat.generate_data(1000,loader.sheet_names,entities)
