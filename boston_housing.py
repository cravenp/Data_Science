#Load Boston Housing dataset from Sklearn.Put the data into a Pandas DataFrame using the data and feature_names attributes 
#from the boston_data object.
#Find the IQR (interquartile range) for AGE, which is defined as the 75th quartile -the 25th quartile.
#Remove observations with an AGE that are not within 1.5 IQR of the median.
#Find the strongest correlated feature with AGE, not including itself, and plot the two features as a scatter plot.  
#Note strongest correlated could mean positive or negative

from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sb

#load data to DF
boston_data = load_boston()
df_boston = pd.DataFrame(boston_data.data,columns=boston_data.feature_names)
df_boston['target'] = pd.Series(boston_data.target)
print(df_boston.head())

#find IRQ
q1 = df_boston['AGE'].quantile(0.25)
q3 = df_boston['AGE'].quantile(0.75)
irq = Q3 - Q1
print("Lower:", q1, "Upper:", q3, "IRQ:", irq)

#remove obs from AGE not within 1.5 IRQ of median
irq_update = irq *1.5
q1_update = q1 - irq_update
q3_update = q3 - irq_update


df_IRQ = df_boston[(df_boston["AGE"]<= q3_update) & (df_boston["AGE"]>= q1_update)]
print("IRQ range:", df_IRQ)

#run correlation using filtered data
dF_boston_corr = df_IRQ.corr(method='pearson')

#make correlations all positive with absolute value
absolute_values = df_boston_corr["AGE"].abs().sort_values().reset_index()
print("Absolute sorted values", absolute_values)

#find strongest correlation
strong_corr = absolute_values.iloc[-2][0]
print("Strongest corr name", strong_corr)

#plot, one using correlation data of DIS vs AGE, one using df_boston DIS data vs Age
sns.set_theme(style="whitegrid")

plot = sns.scatterplot(x="AGE", y=strong_corr, data=df_boston_corr)
plot2 = sns.scatterplot(x="AGE", y="DIS", data=df_boston)
