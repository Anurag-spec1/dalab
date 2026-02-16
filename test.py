import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\anura\Downloads\income.csv")
print(df['Designation'].unique())


for desig in df['Designation'].unique():
    mask = df['Designation'] == desig
    plt.scatter(df.Age[mask],df.Income[mask],label=desig)

plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Age vs Income by Designation')
plt.legend()

plt.scatter([35],[130000],label='New Employee',color='black')
plt.show()