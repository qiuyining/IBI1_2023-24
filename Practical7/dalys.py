# import python libraries 
import os  
import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np  
# Change the working directory to where the dataset is located.
os.chdir("D:/IBI/IBI_git/IBI1_2023-24/Practical7")
# Print the current working directory 
print(os.getcwd())
# List files in the current directory
print(os.listdir("."))
# use the pandas library to read the content of the .csv file into a dataframe object
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())
print(dalys_data.iloc[0,3])
print(dalys_data.iloc[2,0:5])
print(dalys_data.iloc[0:2,:])
print(dalys_data.iloc[0:10:2,0:5])

#show the fourth column (the DALYs) from every 10th row, starting from the first row, for the first 100 rows
print(dalys_data.iloc[0:101:10,3])

my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3,my_columns])

print(dalys_data.loc[2:4,"Year"])
print(dalys_data.loc[0:29,"DALYs"])

#select DALYs for Afghanistan
afghanistan_days=dalys_data.loc[dalys_data['Entity']=='Afghanistan','DALYs']
print(afghanistan_days)

# make an object called china_data to store only the data from China
china_data = dalys_data.loc[dalys_data['Entity'] == 'China', ["Entity", "Year", "DALYs"]]
# Calculate the mean DALYs for China
mean_dalys_china = np.mean(china_data["DALYs"])
print("Mean DALYs in China over time:", mean_dalys_china)

# compare the DALYs in China in 2019 to the mean.
daly_2019 = china_data.loc[china_data["Year"] == 2019, "DALYs"].values[0]
if daly_2019 > mean_dalys_china:
    print("DALYs in 2019 is above the mean.")
elif daly_2019 < mean_dalys_china:
    print("DALYs in 2019 is below the mean.")
else:
    print("DALYs in 2019 is equal to the mean.")
# DALYs in 2019 is below the mean.

# draw plots for china data
plt.plot(china_data.Year, china_data.DALYs, 'b+')
plt.xticks(china_data.Year,rotation=-90)
plt.title("DALYs in China over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.show()
plt.clf

#question part
#Plot a boxplot of DALYs across countries in 2019
year_2019_data = dalys_data[dalys_data["Year"] == 2019]
plt.figure()
plt.boxplot(year_2019_data["DALYs"],vert= False)
plt.xlabel('DALYs')
plt.ylabel('Countries')
plt.title("Boxplot of DALYs across Countries in 2019")
plt.grid(True)
plt.show()
plt.clf



