import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\anura\Downloads\archive\bodyfat.csv")
print(df['Age'].unique())


for desig in df['Age'].unique():
    mask = df['Age'] == desig
    plt.scatter(df.Age[mask],df.BodyFat[mask],label=desig)

plt.xlabel('Age')
plt.ylabel('Body Fat')
plt.title('Age vs Body Fat by Age Group')
plt.show()