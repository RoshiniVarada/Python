import pandas as pd

train_df = pd.read_csv('./train.csv')
train_df["Sex"] = train_df["Sex"].map({'female':1,'male':0}).astype(int)
print("Correalation between Sex and Survived:",train_df["Sex"].corr(train_df["Survived"]))
