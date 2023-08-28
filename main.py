# This is fin_tech_test
# A crypto predictor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from seaborn import regression
import os
for dirname, _, filenames in os.walk('C:/python/fin_tech_test/Lib/archive'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

sns.set_style("whitegrid")
data = pd.read_csv("C:/python/fin_tech_test/Lib/archive/coin_XRP.csv")
print(data.head())
plt.figure(figsize=[10,4])
plt.title("XRP")
plt.xlabel("Price")
plt.ylabel("Volume")
#plt.show(data)
plt.show()


