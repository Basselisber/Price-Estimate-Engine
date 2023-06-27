from enum import Enum
import random

class Country(str, Enum):
    AFGHANISTAN = 'Afghanistan'
    BAHRAIN = 'Bahrain'
    CYPRUS = 'Cyprus'
    EGYPT = 'Egypt'
    IRAN = 'Iran'
    IRAQ = 'Iraq'
    PALESTINE = 'Palestine'
    JORDAN = 'Jordan'
    KUWAIT = 'Kuwait'
    LEBANON = 'Lebanon'
    OMAN = 'Oman'
    PAKISTAN = 'Pakistan'
    QATAR = 'Qatar'
    SAUDI_ARABIA = 'Saudi Arabia'
    SYRIA = 'Syria'
    TURKEY = 'Turkey'
    UNITED_ARAB_EMIRATES = 'United Arab Emirates'
    YEMEN = 'Yemen'
    ALGERIA = 'Algeria'

# for country in Country:
#     print(country) # prints the name of the country
#     print(country.value)
rand = random.choice(list(Country)).value
print(rand)

test = [0.05,0.1,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]
print(len(test))
print(Country.__len__())
print(random.choices(population=list(Country),weights=test))
print(random.uniform(1,199))
