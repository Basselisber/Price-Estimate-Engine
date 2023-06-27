class Column:
    def __init__(self, column_name, column_type):
        self.column_name = column_name
        self.column_type = column_type
        self.column_values = []
    def add_value(self, value):
        self.column_values.append(value)
    def get_values(self):
        return self.column_values
    


    
class Entity:
    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.entity_columns = {'name': Column('name', str),
                               'manufacturer': Column('manufacturer', str),
                               'year': Column('year', int),
                               'price': Column('price', float),}

    def get_column(self, column_name):
        return self.entity_columns.get(column_name)
    def get_column_names(self):
        return self.entity_columns.keys()
    
    
    
    
        