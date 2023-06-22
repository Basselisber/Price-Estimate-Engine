import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant
from statsmodels import *
from itertools import combinations

# Read in the data
df = pd.read_csv('data/Guber1999data.csv')
#dfHead = df.head()

# Create our X and Y variables to run the regression
X = df[['Spend']]
Y = df[['SATT']]

# Run the regression
model = OLS(Y, add_constant(X)).fit()
print(model.summary())

#print(summary)