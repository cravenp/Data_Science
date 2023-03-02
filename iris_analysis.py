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

#Q3
#Using the describe method and loc, find the standard deviation and mean for Sepal Length and Petal Length. 
#Create a new DataFrame that is subset to include only rows where the Sepal Length and Petal Length are greater 
#than one standard deviation from the mean. 
#Find the pairwise correlations for the subset DataFrame and the number of rows left. 
#Do the same but switch the "and" to an "or" when subsetting the DataFrame.

from sklearn.datasets import load_iris 
import numpy as np
import pandas as pd


#load data
iris_data = load_iris()
iris_df1= pd.DataFrame(data= np.c_[iris_data['data'],  iris_data['target']],
                 columns= iris_data['feature_names'] + ['target'])

iris_df1.index.names = ["ID"]

#make df to filter columns
iris_df2 = iris_df1.loc[:,["sepal length (cm)", "petal length (cm)"]]
print(iris_df2.describe())

#make 1 stdev for each column
sepal_length_std = iris_df2.describe()["sepal length (cm)"] ['std']
sepal_length_mean = iris_df2.describe()["sepal length (cm)"] ['mean']
_std_sepal = sepal_length_std + sepal_length_mean

petal_length_std = iris_df2.describe()["petal length (cm)"] ['std']
petal_length_mean = iris_df2.describe()["petal length (cm)"] ['mean']
_std_petal = petal_length_std + petal_length_mean

#filter out with AND
final_df_AND = iris_df2[(iris_df2['sepal length (cm)'] > _std_sepal) & (iris_df2["petal length (cm)"] >_std_petal)]
print(final_df_AND)
print("Length AND:", len(final_df))

#make DF that has items greater than 1 std of the mean using AND
final_df_AND_corr = final_df_AND.corr(method='pearson')
print(final_df_AND_corr)


#final_df.corr swapped using "OR"
final_df_OR = iris_df2[(iris_df2['sepal length (cm)'] > _std_sepal) | (iris_df2["petal length (cm)"] >_std_petal)]
print(final_df_OR)
print("Length OR:", len(final_df_OR))

#make DF that has items greater than 1 std of the mean using OR
final_df_OR_corr = final_df_or.corr(method='pearson')
print(final_df_OR_corr)



#sum across rows
dfarray_sum = dfarray.sum(axis = 1)

#find sums greater than 10, print number of rows greater than 10
sum_df = dfarray_sum[dfarray_sum >10]
print("Sum of individual rows:", sum_df)
print("Rows that are greater than 10:", sum_df)
