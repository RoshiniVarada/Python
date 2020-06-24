import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

plt.style.use(style='ggplot')

train = pd.read_csv(Path('./train.csv'))

# To identify the outliers borders
print(train.describe());
plt.rcParams['figure.figsize']=(10,6)
plt.scatter(train.GarageArea, train.SalePrice, alpha=.5, color='r')
plt.xlabel('Garage area')
plt.ylabel('Sales Price')
plt.show()



filter_data = train[(train.GarageArea > 365) & (train.GarageArea < 1095) & (train.SalePrice < 214000)]
plt.scatter(filter_data.GarageArea, filter_data.SalePrice, alpha=.5, color='b')
plt.xlabel('Garage area')
plt.ylabel('Sales Price')
plt.show()

