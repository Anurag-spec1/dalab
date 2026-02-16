import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df=pd.read_csv(r"C:\Users\anura\Downloads\archive\bodyfat.csv")
print(df['Age'].unique())


for desig in df['Age'].unique():
    mask = df['Age'] == desig
    plt.scatter(df.Age[mask],df.BodyFat[mask],label=desig)

plt.xlabel('Age')
plt.ylabel('Body Fat')
plt.title('Age vs Body Fat by Age Group')
plt.legend()

plt.scatter([50],[40],label='New Disease',color='black')

plt.show()


model=KNeighborsClassifier(n_neighbors=3)
model

x = df.drop(columns=["Chest", "BodyFat"])
y = df["BodyFat"]

print(x.info())
print(y.info())    

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1) 
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

model.fit(x_train,y_train)


print(model.predict([[50, 40]]))