# import required modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# read csv as dataframe using pandas module
df = pd.read_csv('train.csv')
print(df.head(6))

# ============================================
# Divide columns from 0-4 5-9 and so on.

bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
labels=['00-04','05-09','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84']

df["AgeGroup"] = ""

for index, row in df.iterrows():
    # print(pd.isna(row["Age"]))
    if not pd.isna(row["Age"]):
        # print(row["Age"]/5, int(row["Age"]/5), labels[int(row["Age"]/5)])
        df.loc[index,"AgeGroup"]=labels[int(row["Age"]/5)]
# print(df.head())

#
# ============================================
# Did age play a significant role?

SurvivedByAge = df.groupby('AgeGroup')['Survived'].mean()
print(SurvivedByAge)

group, rate = np.histogram(SurvivedByAge)
fig1 = plt.figure()
SurvivedByAge.plot(kind = 'bar')
fig1.tight_layout()
plt.show()
plt.savefig("Q1.png", dpi=600, format="png")
# plt.close()

# ============================================
# Checking Conditions for Question 2

df["AgeClass"] = ""
for index, row in df.iterrows():
    if not pd.isna(row["Age"]):
        if row["Age"] <10 or row["Age"] >65:
            df.loc[index,"AgeClass"]="<10 & >65"
        else:
            df.loc[index,"AgeClass"]="11-64"
print(df.head())
# df.to_csv("output2.csv")

SurvivedByAgeclass = df.groupby('AgeClass')['Survived'].mean()
print(SurvivedByAgeclass)

group, rate = np.histogram(SurvivedByAge)
fig2 = plt.figure()
SurvivedByAgeclass.plot(kind = 'bar')
fig2.tight_layout()
plt.show()
plt.savefig("Q2.png", dpi=600, format="png")

# plt.close()