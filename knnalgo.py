from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\anura\Downloads\income.csv")

model=KNeighborsClassifier(n_neighbors=3)
model

x = df.drop(columns=["Designation"])
y = df["Designation"]

print(x.info())
print(y.info())    