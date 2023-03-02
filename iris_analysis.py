#Q1
#Import the load_iris() function from SkLearn. Make two DataFrames. 
#The first should have the 4 numeric features and a target column that is the id of the species.
#The second should be a lookup, with target id and the corresponding Species.  
#Join the two together so the first DataFrame has the species names appended.
#Once joined, make a bar plot of the standard deviations by species (use the name not the id).

from sklearn.datasets import load_iris 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load data
iris_data = load_iris()
iris_df1= pd.DataFrame(data= np.c_[iris_data['data'],], 
                 columns= iris_data['feature_names'])

iris_df1.index.names = ["ID"]
print(iris_df1)


#lookup with ID and species

iris_df1['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
iris_df2 = iris_df1.iloc[:,4]
print(iris_df1['species'])

#test look ups
print("Lookup test", iris_df2[145])
assert iris_df2[145] == "virginica"
assert iris_df2[1] == 'setosa'

#combine dfs
iris_df1.append(iris_df2)
print("Final DF", iris_df1)
std = iris_df1.groupby(["species"]).std()
print(std)
    

#make plots

plt.figure(figsize=(10,5))
ax = sns.barplot(x = "species", y = "sepal length (cm)", data = iris_df1, estimator = np.std)
ax.set_xlabel("Species", fontsize = 10)
ax.set_ylabel("Standard Deviation", fontsize = 10)
ax.set_title("Standard Deviation of Sepal Length by Species", fontsize = 15)

plt.figure(figsize=(10,5))
ax = sns.barplot(x = "species", y = "sepal width (cm)", data = iris_df1, estimator = np.std)
ax.set_xlabel("Species", fontsize = 10)
ax.set_ylabel("Standard Deviation", fontsize = 10)
ax.set_title("Standard Deviation of Sepal Width by Species", fontsize = 15)

plt.figure(figsize=(10,5))
ax = sns.barplot(x = "species", y = "petal length (cm)", data = iris_df1, estimator = np.std)
ax.set_xlabel("Species", fontsize = 10)
ax.set_ylabel("Standard Deviation", fontsize = 10)
ax.set_title("Standard Deviation of Petal Length by Species", fontsize = 15)

plt.figure(figsize=(10,5))
ax = sns.barplot(x = "species", y = "petal width (cm)", data = iris_df1, estimator = np.std)
ax.set_xlabel("Species", fontsize = 10)
ax.set_ylabel("Standard Deviation", fontsize = 10)
ax.set_title("Standard Deviation of Petal Width by Species", fontsize = 15)



#Q2
#Using the Iris dataset, sum the 4 numeric features and find out how many rows have a sum greater than 10.  
#Do this in two ways.  
#Solve this using both Pandas and Numpy.

from sklearn.datasets import load_iris 
import numpy as np
import pandas as pd


#load data
iris_data = load_iris()

#make into array
array = np.array(iris_data.data)
print(array.shape)

#sum across rows sepal length, width, petal length, width
sum_array = array.sum(axis = 1)
print("Sum of individual rows:", sum_array)
sum_array_final = sum_array > 10
print("Rows greater than 10:", sum_array_final)

# count how many rows
sum_rows = sum_array_final.sum()
print("Number of rows greater than 10:", sum_rows)

#Pandas
#make dataframe
dfarray = pd.DataFrame(iris_data.data)
print(dfarray)

#sum across rows
dfarray_sum = dfarray.sum(axis = 1)

#find sums greater than 10, print number of rows greater than 10
sum_df = dfarray_sum[dfarray_sum >10]
print("Sum of individual rows:", sum_df)
print("Rows that are greater than 10:", sum_df)
